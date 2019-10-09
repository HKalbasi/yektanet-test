from django.shortcuts import render, redirect, get_object_or_404
from .models import Advertiser, Ad, Click, View
from django.views.generic.base import TemplateView, RedirectView, View as ClassView
from datetime import datetime, timedelta
from django.http import Http404
from django.db.models import Count

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
    res = {}
    for ad in ads:
      res[ad.id] = { 'table' : [], 'title': ad.title, 'click_count': 0, 
        'view_count': 0, 
        'rate': '-',
        'dis_av': '-',
      }
    clickCount = Click.objects.values('owner').annotate(count=Count('id'))
    viewCount  = View .objects.values('owner').annotate(count=Count('id'))
    for cc in clickCount:
      res[cc['owner']]['click_count'] = cc['count']
    for vc in viewCount:
      res[vc['owner']]['view_count'] = vc['count']
      res[vc['owner']]['rate'] = res[cc['owner']]['click_count']/vc['count']
    tt = start
    while tt < end:
      nt = tt + timedelta(hours=1)
      cc = Click.objects.values('owner').filter(time__lt = nt , time__gt = tt).annotate(count=Count('id'))
      cv = View .objects.values('owner').filter(time__lt = nt , time__gt = tt).annotate(count=Count('id'))
      for ad in ads:
        res[ad.id]['table'].append({'time': tt.hour, 'clicks': 0, 'views': 0, 'average': '-'})
      for x in cc:
        res[x['owner']]['table'][-1]['clicks'] = x['count']
      for x in cv:
        res[x['owner']]['table'][-1]['views'] = x['count']
        res[x['owner']]['table'][-1]['average'] = res[x['owner']]['table'][-1]['clicks']/x['count']    
      tt = nt
    dis_av_all = Ad.objects.raw(
      """
      SELECT owner_id as id, AVG(diff) as diff
      FROM (
        SELECT 
          a.id, 
          a.owner_id, 
          (JulianDay(a.time)-JulianDay(MAX(b.time)))*24*60*60 as diff 
        FROM advertiser_mangement_click as a 
        INNER JOIN advertiser_mangement_view as b 
        ON a.ip = b.ip AND a.time > b.time AND a.owner_id = b.owner_id 
        GROUP BY a.id
      ) 
      GROUP BY owner_id;
      """
    )
    for x in dis_av_all:
      res[x.id]['dis_av'] = x.diff
    return render (req, "advertiser_mangement/report.html",{
      "res": res,
    })