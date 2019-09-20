from django.shortcuts import render

# Create your views here.
def mainView(req):
  render(req, 'advertiser_management/ads.html',{
    'advertisers' : [],
  })