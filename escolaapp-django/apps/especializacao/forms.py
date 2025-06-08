from django import forms
from .models import Especializacao

class CategoryForm(forms.ModelForm):

    class Meta:
        model = Especializacao
        exclude = ()