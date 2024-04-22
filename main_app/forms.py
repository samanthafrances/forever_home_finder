from django import forms
from .models import AdoptionInquiry

class AdoptionInquiryForm(forms.ModelForm):
    class Meta:
        model = AdoptionInquiry
        fields = ['name', 'email', 'message']