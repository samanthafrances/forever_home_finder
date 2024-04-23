from django.urls import path
from . import views
from .views import profile


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('volunteer/', views.volunteer_view, name='volunteer'),
    path('blog/', views.blog_view, name='blog'),
    path('donate/', views.donate_view, name='donate'),
    path('messaging/', views.messaging, name='messaging'),
    path('resources/', views.resources, name='resources'),
    path('petitions/', views.petitions_view, name='petitions'),
    path('adoption/', views.adoption, name='adoption'),
    path('search/', views.search_animals, name='search_animals'),
    path('adopt/<int:animal_id>/', views.adopt_animal, name='adopt_animal'),
    path('blog/<int:blog_id>/assoc_sub/<int:user_id>/', views.assoc_sub, name='assoc_sub'),
    path('accounts/register/', views.register, name='register'),
    path('adoption/<int:animal_id>/', views.adoption_details, name='adoption_details'),
    path('blog/<int:blog_id>/', views.blog_details, name='blog_details'),
    path('profile/', profile, name='profile'),
<<<<<<< Updated upstream
    path('blog/<int:blog_id>/', views.blog_details, name='blog_details'),
    path('messageform/', views.CreateMessage.as_view(), name='messageform' ),
    path('messaging/<int:pk>/update', views.UpdateMessage.as_view(), name='message_update'),
    path('messaging/<int:pk>/delete',views.DeleteMessage.as_view(), name='message_delete')
=======
     path('blog/<int:blog_id>/', views.blog_details, name='blog_details'),
     path('messageform/', views.CreateMessage.as_view(), name='messageform'),
     path('upload-profile-picture/', views.upload_profile_picture, name='upload_profile_picture'),
>>>>>>> Stashed changes
]




