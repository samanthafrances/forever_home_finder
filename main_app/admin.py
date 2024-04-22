from django.contrib import admin
from .models import Animal, Blog, Subscriber, Comment, Message, Profile 

# Register your models here.
admin.site.register(Animal)
admin.site.register(Blog)
admin.site.register(Subscriber)
admin.site.register(Comment)
admin.site.register(Message)
admin.site.register(Profile)