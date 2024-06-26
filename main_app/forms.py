from django import forms
from .models import AdoptionInquiry, Profile, Comment, Message
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class AdoptionInquiryForm(forms.ModelForm):
    class Meta:
        model = AdoptionInquiry
        fields = ['name', 'email', 'message']
        
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
class ProfilePictureForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar']
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 3})
        }
        
class ReplyForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3}),
        }