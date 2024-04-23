
from django.shortcuts import render, redirect, get_object_or_404
from .models import User, Blog, Animal, Subscriber, Message
from .forms import AdoptionInquiryForm, CustomUserCreationForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required

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

def petitions_view(request):
 return render(request, 'sign-petitions.html')

def messaging(request):
  return render(request, 'messaging.html')

def resources(request):
  return render(request, 'resources.html')

def adoption(request):
  animals = Animal.objects.all()
  return render(request, 'adoption.html', {'animals': animals})

def search_animals(request):
    query = request.GET.get('query')
    animals = Animal.objects.filter(species__icontains=query) | Animal.objects.filter(breed__icontains=query)
    return render(request, 'adoption.html', {'animals': animals})

def adopt_animal(request, animal_id):
    animal = Animal.objects.get(id=animal_id)
    return render(request, 'adopt_animal.html', {'animal': animal})
  
def adopt_animal(request, animal_id):
    animal = Animal.objects.get(pk=animal_id)
    if request.method == 'POST':
        form = AdoptionInquiryForm(request.POST)
        if form.is_valid():
            inquiry = form.save(commit=False)
            inquiry.animal = animal
            inquiry.save()
            return redirect('/') 
    else:
        form = AdoptionInquiryForm()
    return render(request, 'adoption.html', {'form': form, 'animal': animal})

def assoc_sub(request, blog_id, user_id):
   Blog.objects.get(id=blog_id).subscribers.add(user_id)
   return redirect('blog')

def register(request):
    error_message = ''
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
        else:
            error_message = 'Invalid sign up - try again'
    else:
        form = CustomUserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/register.html', context)

def adoption_details(request, animal_id):
    animal = get_object_or_404(Animal, pk=animal_id)
    return render(request, 'adoptiondetails.html', {'animal': animal})

def blog_details(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog-detail.html', {'post': blog})

@login_required
def profile(request):
    return render(request, 'profile.html')

# Messaging functionality

class CreateMessage(CreateView) :
  template_name = 'message_form.html'
  success_url = '/messaging/'
  model = Message
  fields = ['content']

class UpdateMessage :
  model = Message
  fields = ['content']

class DeleteMessage :
   model = Message
   










