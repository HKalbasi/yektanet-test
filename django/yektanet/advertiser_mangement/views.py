from django.shortcuts import render, redirect, get_object_or_404
from .models import Advertiser, Ad
from django.views.generic.base import TemplateView, RedirectView

# Create your views here.
class IndexView(TemplateView):
  template_name = "advertiser_mangement/ads.html"

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    advertiser_array = Advertiser.objects.order_by('-name')
    for advertiser in advertiser_array:
      advertiser.ads = Ad.objects.filter(owner = advertiser)  
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

class AdminApprove(TemplateView):
  template_name = "advertiser_mangement/admin_approve.html"
  def get_context_data(self, **kwargs):
    context['ads'] = Ad.objects.filter(approved = False).all()
    return context
