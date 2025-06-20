from django import forms
from .models import Enrollment

class ClientForm(forms.ModelForm):

    class Meta:
        model = Enrollment
        exclude = ('created_on', 'updated_on')
