from django.shortcuts import render
from .models import Advertiser, Ad

# Create your views here.
def index(req):
  advertiser_array = Advertiser.objects.order_by('-name')
  for advertiser in advertiser_array:
    advertiser.ads = Ad.objects.filter(owner = advertiser)
  return render(req, 'advertiser_mangement/ads.html',{
    'advertisers' : advertiser_array,
  })