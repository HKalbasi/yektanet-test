from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('click/<ad_id>/', views.ClickView.as_view(), name='click'),
    path('new_ad/', views.new_ad, name='new_ad'),
    path('admin/approve/', views.AdminApprove.as_view(), name='admin_approve'),
]