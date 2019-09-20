from django.shortcuts import render

# Create your views here.
def index(req):
  return render(req, 'advertiser_mangement/ads.html',{
    'advertisers' : [],
  })