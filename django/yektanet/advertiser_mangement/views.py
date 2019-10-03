from django.shortcuts import render, redirect, get_object_or_404
from .models import Advertiser, Ad, Click, View
from django.views.generic.base import TemplateView, RedirectView, View as ClassView
from datetime import datetime, timedelta
from django.http import Http404

# Create your views here.
class IndexView(TemplateView):
  template_name = "advertiser_mangement/ads.html"

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    advertiser_array = Advertiser.objects.order_by('-name')
    for advertiser in advertiser_array:
      advertiser.ads = Ad.objects.filter(approved = 'OK', owner = advertiser)
      for ad in advertiser.ads:
        ad.incViews(self.request.IP)
    context['advertisers'] = advertiser_array
    return context

class ClickView(RedirectView):
  def get_redirect_url(self, ad_id):
    the_ad = get_object_or_404(Ad, id = ad_id)
    the_ad.incClicks(self.request.IP)
    return the_ad.link

class NewAdView(ClassView):
  def post(self, req):
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
  def get(self, req):
    return render(req, 'advertiser_mangement/new_ad.html')

class ReportSelectTimeView(TemplateView):
  template_name = "advertiser_mangement/report-select-time.html"
  def get_context_data(self, **kwargs):
    if not self.request.user.is_staff:
      raise Http404()

class ReportView(ClassView):
  def get(self, req):
    if not req.user.is_staff:
      raise Http404()
    ads = Ad.objects.all()
    try:
      start = datetime.strptime(req.GET['start'],"%Y-%m-%d-%H")
      end   = datetime.strptime(req.GET['end'],"%Y-%m-%d-%H")
    except Exception as e:
      return redirect('/report/select_time/')
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
      tt = start
      ad.table = []
      while tt < end:
        nt = tt + timedelta(hours=1)
        cc = clicks.filter(time__lt = nt , time__gt = tt).count()
        cv = views .filter(time__lt = nt , time__gt = tt).count()
        ad.table.append({
          'time'    : tt.hour,
          'clicks'  : cc,
          'views'   : cv,
          'average' : cc/max(cv,1)
        })
        tt = nt
      ad.dis_av = diff / max(clicks.count(),1)
      ad.rate = clicks.count() / max(views.count(),1)
    return render (req, "advertiser_mangement/report.html",{
      "ads": ads
    })