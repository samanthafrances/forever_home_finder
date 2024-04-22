from django import forms
from .models import AdoptionInquiry
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