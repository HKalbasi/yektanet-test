from django.urls import path

from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('click/<ad_id>/', views.click, name='click'),
    path('new_ad/', views.new_ad, name='new_ad'),
]