from django.urls import path, include

from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('advertiser', AdvertiserViewSet)
router.register('ad', AdViewSet)

urlpatterns = [
  path('api-auth/', include('rest_framework.urls')),
  path('report/<startString>/<endString>/', ReportView.as_view()),
  path('', include(router.urls)),
]