from django import forms
from cliente.models import Cliente
    
class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        exclude = ['endereco']
