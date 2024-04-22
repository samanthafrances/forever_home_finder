from django.shortcuts import render
from .models import User

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def volunteer_view(request):
    return render(request, 'volunteer.html')

def blog_view(request):
    return render(request, 'blog.html')


def donate_view(request):
    return render(request, 'donate.html')

def messaging(request):
  return render(request, 'messaging.html')

def resources(request):
  return render(request, 'resources.html')

def adoption(request):
  return render(request, 'adoption.html')




def assoc_sub(request, user_id):
   user = User.objects.get(id=user_id)
   user.subscriber.add(user)








