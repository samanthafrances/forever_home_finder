
from django.shortcuts import render, redirect, get_object_or_404
from .models import User, Blog, Animal, Subscriber, Message, Profile, Comment
from .forms import AdoptionInquiryForm, CustomUserCreationForm, ProfilePictureForm, CommentForm, ReplyForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.urls import reverse_lazy

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
   messages = Message.objects.all()
   context = {'messages': messages}
   return render(request, 'messaging.html', context)

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
    comments = blog.comments.all()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog = blog
            comment.user = request.user
            comment.save()
            return redirect('blog_details', blog_id=blog_id)
    else:
        form = CommentForm()
    return render(request, 'blog-detail.html', {'post': blog, 'comments': comments, 'form': form})

def petitions(request):
    petitions = [
        {
            'url': 'https://www.change.org/p/demand-felony-charges-against-cody-roberts-for-animal-cruelty?',
            'image': 'https://assets.change.org/photos/4/lx/fr/HpLXFRqHHuLoLxE-800x450-noPad.jpg?1712441239',
            'title': 'Demand Felony Charges Against Cody Roberts for Animal Cruelty',
            'description': 'Please join us in standing up against such heinous acts of violence towards our wildlife by signing this petition today!',

            'url': 'https://www.change.org/p/let-ukraine-s-refugee-animals-live?',
            'image': 'https://assets.change.org/photos/2/oa/rh/rboArhVoZOmrTnx-800x450-noPad.jpg?1688372973',
            'title': 'Let Ukraine’s refugee animals live!',
            'description': 'Pets don’t start wars, they are helpless against human cruelty, shocked by bombs and missiles, and are entirely dependent on us for their survival.',

            'url': 'https://www.change.org/p/make-texas-safe-for-animals?',
            'image': 'https://assets.change.org/photos/8/sb/ea/YYsbEaRynLrjbym-800x450-noPad.jpg?1640306464',
            'title': 'Make Texas Safe For Animals',
            'description': 'Awareness is the first step towards change so please sign our petition in hope  to bring an everlasting change for animals in the state of Texas.',

            'url': 'https://www.change.org/p/government-ban-wild-animals-trading-locally-and-internationally?',
            'image': 'https://assets.change.org/photos/2/wb/us/RPWbUswzJMlNXqc-800x450-noPad.jpg?1580272081',
            'title': 'BAN wild animals trading locally and internationally',
            'description': 'Let’s work together to stop and permanently ban the trading of wild animals. If we don’t stop this now, it will happen again.',

            'url': 'https://www.change.org/p/craigslist-end-the-selling-of-animals-on-craigslist?',
            'image': 'https://assets.change.org/photos/5/mn/jr/almnJRXMPpHUzCc-800x450-noPad.jpg?1614913812',
            'title': 'End the Selling of Animals on Craigslist',
            'description': 'Craigslist can end the exploitation of these animals by banning the transfer of all animals on its website.',

            'url': 'https://www.change.org/p/seaworld-stop-exploiting-animals-for-human-entertainment?',
            'image': 'https://assets.change.org/photos/1/qv/zd/JaQVzDXGvKSopZl-800x450-noPad.jpg?1658380547',
            'title': 'SeaWorld: STOP exploiting animals for human entertainment.',
            'description': 'Please sign and share this petition calling on Sea World to free the dolphins so we can create meaningful change.',

            'url': 'https://www.change.org/p/l-or%C3%A9al-ban-l-or%C3%A9al-from-testing-on-animals?',
            'image': 'https://assets.change.org/photos/7/iq/oa/lmiQoAZtRuJeTxf-800x450-noPad.jpg?1581491971',
            'title': 'Ban L’Oréal from Testing on Animals',
            'description': 'Animal testing is a barbaric deed that is carried out by companies worldwide.',

            'url': 'https://www.change.org/p/ebay-classifieds-stop-selling-live-animals?',
            'image': 'https://assets.change.org/photos/4/le/js/HRLEjsYUHYHuXzL-800x450-noPad.jpg?1515770546',
            'title': 'Ebay Classifieds: Stop Selling Live Animals',
            'description': 'They are providing a vast marketplace for puppy mills to sell dogs and by doing this they are contributing to animal cruelty.',

            'url': 'https://www.change.org/p/brock-urge-fema-to-save-millions-of-farm-animals?',
            'image': 'https://assets.change.org/photos/2/jy/sd/xRJYSDGdNSMrfkK-800x450-noPad.jpg?1537552198',
            'title': 'Urge FEMA to save millions of farm animals',
            'description': 'Sign today to tell FEMA to protect farm animals in the PETS Act.',

            'url': 'https://www.change.org/p/universoul-circus-stop-using-animals-as-props-in-your-show?',
            'image': 'https://assets.change.org/photos/5/kf/vz/xskfVzzItYlQVqu-800x450-noPad.jpg?1523033601',
            'title': 'UniverSoul Circus: Stop Using Animals As Props In Your Show!',
            'description': 'Now more than ever people are becoming increasingly aware of the inherent cruelty of the animal entertainment industry.',
        },
    ]
    return render(request, 'petitions.html', {'petitions': petitions})

@login_required
def profile(request):
    return render(request, 'profile.html')

@login_required
def upload_profile_picture(request):
    if request.method == 'POST':
        form = ProfilePictureForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfilePictureForm(instance=request.user.profile)
    return render(request, 'upload_profile_picture.html', {'form': form})

def change_username(request):
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserChangeForm(instance=request.user)
    return render(request, 'change_username.html', {'form': form})

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('profile')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'change_password.html', {'form': form})

def reply_message(request, message_id):
    message = Message.objects.get(pk=message_id)
    if request.method == 'POST':
        form = ReplyForm(request.POST)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.user = request.user
            reply.parent_message = message  
            reply.save()
            return redirect('messaging')
    else:
        form = ReplyForm()
    return render(request, 'reply_message.html', {'form': form, 'message': message})

# Messaging functionality
class CreateMessage(CreateView) :
  template_name = 'message_form.html'
  success_url = '/messaging'
  model = Message
  fields = ['content']
  
class UpdateMessage(UpdateView) :
  model = Message
  fields = ['content']
  template_name = 'edit_message.html'
  success_url = reverse_lazy('messaging')

class DeleteMessage(DeleteView) :
   model = Message
   success_url = reverse_lazy('messaging')
   template_name = 'delete_message.html'
   










