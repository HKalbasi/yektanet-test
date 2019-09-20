from django.shortcuts import render, redirect, get_object_or_404
from .models import Advertiser, Ad

# Create your views here.
def index(req):
  advertiser_array = Advertiser.objects.order_by('-name')
  for advertiser in advertiser_array:
    advertiser.ads = Ad.objects.filter(owner = advertiser)
  return render(req, 'advertiser_mangement/ads.html',{
    'advertisers' : advertiser_array,
  })

def click(req, ad_id):
  the_ad = get_object_or_404(Ad, id = ad_id)
  the_ad.incClicks()
  return redirect(the_ad.link)