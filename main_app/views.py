from django.shortcuts import render
from .models import User, Blog, Subscriber

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




def assoc_sub(request, blog_id, user_id):
   Blog.objects.get(id=blog_id).subscribers.add(user_id)
   return redirect('blog')








