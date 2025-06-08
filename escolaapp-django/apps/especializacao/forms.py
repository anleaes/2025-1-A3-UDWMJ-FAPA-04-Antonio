from django import forms
from .models import Especializacao

class EspecializacaoForm(forms.ModelForm):

    class Meta:
        model = Especializacao
        exclude = ()