from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('volunteer/', views.volunteer_view, name='volunteer'),
    path('blog/', views.blog_view, name='blog'),
    path('donate/', views.donate_view, name='donate'),
]