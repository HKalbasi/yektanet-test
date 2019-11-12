from django.contrib.auth.models import User

from rest_framework import routers, serializers, viewsets
from .models import Advertiser, Ad

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = User
    fields = ['url', 'username', 'email', 'is_staff']

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
  queryset = User.objects.all()
  serializer_class = UserSerializer

class AdvertiserSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Advertiser
    fields = ['name']

# ViewSets define the view behavior.
class AdvertiserViewSet(viewsets.ModelViewSet):
  queryset = Advertiser.objects.all()
  serializer_class = AdvertiserSerializer

class AdSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Ad
    fields = ['title', 'imgUrl', 'link', 'owner', 'approved']

# ViewSets define the view behavior.
class AdViewSet(viewsets.ModelViewSet):
  queryset = Ad.objects.all()
  serializer_class = AdSerializer


router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('advertiser', AdvertiserViewSet)
router.register('ad', AdViewSet)