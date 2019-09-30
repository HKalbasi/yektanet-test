from django.shortcuts import render, redirect, get_object_or_404
from .models import Advertiser, Ad, Click, View
from django.views.generic.base import TemplateView, RedirectView, View as ClassView
from datetime import datetime, timedelta

# Create your views here.
class IndexView(TemplateView):
  template_name = "advertiser_mangement/ads.html"

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    advertiser_array = Advertiser.objects.order_by('-name')
    for advertiser in advertiser_array:
      advertiser.ads = Ad.objects.filter(approved = 'OK', owner = advertiser)
      for ad in advertiser.ads:
        ad.incViews(self.request.META['REMOTE_ADDR'])
    context['advertisers'] = advertiser_array
    return context

class ClickView(RedirectView):
  def get_redirect_url(self, ad_id):
    the_ad = get_object_or_404(Ad, id = ad_id)
    the_ad.incClicks(self.request.META['REMOTE_ADDR'])
    return the_ad.link

def new_ad(req):
  if req.method == 'POST':
    try:
      owner = Advertiser.objects.get(id = req.POST['owner_id'])
      Ad.objects.create(
        title  = req.POST['title'],
        owner  = owner,
        imgUrl = req.POST['image_url'],
        link   = req.POST['link'],
      )
      return redirect('/')
    except Exception as e:
      return render(req, 'advertiser_mangement/new_ad.html', {
        'error_message': 'Error ' + repr(e),
      })
  else:
    return render(req, 'advertiser_mangement/new_ad.html')

class ReportView(TemplateView):
  template_name = "advertiser_mangement/report.html"

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    ads = Ad.objects.all()
    for ad in ads:
      clicks = Click.objects.filter(owner = ad)
      views = View.objects.filter(owner = ad)
      diff = 0
      for click in clicks:
        view =  views.filter(ip = click.ip, time__lt = click.time).order_by('-time').first()
        if view == None:
          raise "what?"
        else:
          diff += (click.time - view.time).total_seconds()
      tt = datetime.today()
      ad.table = []
      for x in range(24):
        nt = tt - timedelta(hours=1)
        cc = clicks.filter(time__gt = nt , time__lt = tt).count()
        cv = views.filter(time__gt  = nt , time__lt = tt).count()
        ad.table.append({
          'time'    : tt.hour,
          'clicks'  : cc,
          'views'   : cv,
          'average' : cc/max(cv,1)
        })
        tt = nt
      ad.dis_av = diff / max(clicks.count(),1)
      ad.rate = clicks.count() / max(views.count(),1)
    context['ads'] = ads
    return context