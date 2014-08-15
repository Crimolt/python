from django import forms
from parceiro.models import Parceiro
    
class ParceiroForm(forms.ModelForm):
    class Meta:
        model = Parceiro
        exclude = ['endereco']
