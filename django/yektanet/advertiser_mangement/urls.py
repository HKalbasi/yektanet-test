from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('report/select_time/', views.ReportSelectTimeView.as_view(), name='report_select_time'),
    path('report/', views.ReportView.as_view(), name='report'),
    path('click/<ad_id>/', views.ClickView.as_view(), name='click'),
    path('new_ad/', views.NewAdView.as_view(), name='new_ad'),
]