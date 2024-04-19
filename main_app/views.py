from django.shortcuts import render

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
