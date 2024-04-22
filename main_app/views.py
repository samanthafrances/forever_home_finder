from django.shortcuts import render
from .models import User, Blog

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def volunteer_view(request):
    return render(request, 'volunteer.html')

def blog_view(request):
    blog = Blog.objects.all()
    return render(request, 'blog.html', {'blog' : blog})


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
   user.subscriber.add(request.user)








