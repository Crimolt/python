from django import forms
from endereco.models import Endereco
from django.forms.util import ErrorList
    
class EnderecoForm(forms.ModelForm):
	class Meta:
		model = Endereco

	def clean(self):
		cleaned_data = self.cleaned_data

		# for field in cleaned_data:
			# self._errors[field] = field
		
		# Sempre retorne a coleção completa de dados válidos.
		return cleaned_data
