# forms.py
from django import forms
from .models import Glamrush

class GlamrushForm(forms.ModelForm):
    class Meta:
        model = Glamrush
        fields = ['name', 'description', 'price', 'category', 'image']
