from django import forms
from .models import Class

class ClassForm(forms.ModelForm):

    class Meta:
        model = Class
        exclude = ('created_on', 'updated_on')