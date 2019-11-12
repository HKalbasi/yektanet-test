from django.shortcuts import render
from .serializers import AdSerializer, AdvertiserSerializer, UserSerializer
from advertiser_mangement.models import Advertiser, Ad, Click, View
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from datetime import datetime, timedelta
from django.db.models import Count

# Create your views here.

class AdViewSet(viewsets.ModelViewSet):
  queryset = Ad.objects.all()
  serializer_class = AdSerializer

class AdvertiserViewSet(viewsets.ModelViewSet):
  queryset = Advertiser.objects.all()
  serializer_class = AdvertiserSerializer

class UserViewSet(viewsets.ModelViewSet):
  queryset = User.objects.all()
  serializer_class = UserSerializer

class ReportView(APIView):
  permission_classes = [permissions.IsAdminUser]
  def get(self, req, startString, endString):
    ads = Ad.objects.all()
    try:
      start = datetime.strptime(startString,"%Y-%m-%d-%H")
      end   = datetime.strptime(endString,"%Y-%m-%d-%H")
    except Exception as e:
      return Response({"ok": False, "reason": str(e)})
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
    return Response(res)