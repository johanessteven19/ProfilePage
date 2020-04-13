from django import forms
from django.forms import ModelForm
from .models import Data

class DataForm(forms.ModelForm):
    class Meta:
        model = Data
        fields = '__all__'
        
