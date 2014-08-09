from django import forms
from endereco.models import Endereco
    
class EnderecoForm(forms.ModelForm):
    class Meta:
        model = Endereco
