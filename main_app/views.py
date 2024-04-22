
from django.shortcuts import render, redirect
from .models import User, Blog, Animal
from .forms import AdoptionInquiryForm


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








