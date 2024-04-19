from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def messaging(request):
  return render(request, 'messaging.html')

def resources(request):
  return render(request, 'resources.html')

def adoption(request):
  return render(request, 'adoption.html')