from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('volunteer/', views.volunteer_view, name='volunteer'),
    path('blog/', views.blog_view, name='blog'),
    path('donate/', views.donate_view, name='donate'),
    path('messaging/', views.messaging, name='messaging'),
    path('resources/', views.resources, name='resources'),
    path('adoption/', views.adoption, name='adoption'),

]