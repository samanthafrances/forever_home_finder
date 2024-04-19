from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('messaging/', views.messaging, name='messaging'),
    path('resources/', views.resources, name='resources'),
    path('adoption/', views.adoption, name='adoption'),
]