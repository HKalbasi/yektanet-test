from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('click/<ad_id>/', views.click, name='click'),
]