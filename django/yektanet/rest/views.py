from django.shortcuts import render
from .serializers import AdSerializer, AdvertiserSerializer, UserSerializer
from advertiser_mangement.models import Advertiser, Ad
from django.contrib.auth.models import User
from rest_framework import viewsets

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
