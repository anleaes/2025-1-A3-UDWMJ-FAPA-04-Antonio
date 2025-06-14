from django import forms
from .models import Specialization

class SpecializationForm(forms.ModelForm):

    class Meta:
        model = Specialization
        exclude = ('created_on', 'updated_on')