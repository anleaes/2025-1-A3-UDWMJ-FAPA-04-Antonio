from django import forms
from .models import Professor

class ClientForm(forms.ModelForm):

    class Meta:
        model = Professor
        exclude = ()
