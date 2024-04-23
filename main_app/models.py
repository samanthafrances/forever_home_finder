from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Animal(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    age = models.IntegerField()
    breed = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Blog(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    subscribers = models.ManyToManyField(User, through='Subscriber', related_name='subscribers')

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('blog')
    
class Subscriber(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    email = models.EmailField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content
    
class Message(models.Model):
    content = models.TextField()
    

    def __str__(self):
        return self.content
    
    def get_absolute_url(self):
     return reverse('messaging')
    

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    avatar = models.ImageField(upload_to='avatars/', default='avatars/default.jpg')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Profile of {self.user.username}'
    
class AdoptionInquiry(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Inquiry for {self.animal.name} by {self.name}"