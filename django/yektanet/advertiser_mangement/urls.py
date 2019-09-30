from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('report/', views.ReportView.as_view(), name='report'),
    path('click/<ad_id>/', views.ClickView.as_view(), name='click'),
    path('new_ad/', views.new_ad, name='new_ad'),
]