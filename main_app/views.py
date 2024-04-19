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