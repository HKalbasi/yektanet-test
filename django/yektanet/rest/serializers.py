from django.contrib.auth.models import User
from rest_framework import serializers
from advertiser_mangement.models import Advertiser, Ad


class UserSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = User
    fields = ['url', 'username', 'email', 'is_staff']

class AdvertiserSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Advertiser
    fields = ['name']

class AdSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Ad
    fields = ['title', 'imgUrl', 'link', 'owner', 'approved']
