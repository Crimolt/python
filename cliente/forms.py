from django import forms
from cliente.models import Cliente
from django.forms.util import ErrorList

class ClienteForm(forms.ModelForm):
	class Meta:
		model = Cliente
		exclude = ['endereco']
		read_only = ['data_cadastro']

	def clean(self):
		cleaned_data = self.cleaned_data
		nome = cleaned_data.get('nome');

		if 'levi' not in nome:
			self._errors['nome'] = ErrorList(['esqueceu de levi']) 

		# Sempre retorne a coleção completa de dados válidos.
		return cleaned_data