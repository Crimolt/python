#coding: utf-8
from django import forms
from pessoa.models import Pessoa
from django.forms.util import ErrorList
from validation.burocracia import validate_cpf, validate_cnpj

class PessoaForm(forms.ModelForm):
	class Meta:
		model = Pessoa
		exclude = ['endereco']
		read_only = ['data_cadastro']

	def clean(self):
		cleaned_data = self.cleaned_data
		
		if cleaned_data['tipo_pessoa'] == 'F':
			if not validate_cpf(cleaned_data['cpf']):
				self._errors['cpf'] = ErrorList(['CPF inválido'])
		else:
			if not validate_cnpj(cleaned_data['cnpj']):
				self.errors['cnpj'] = ErrorList(['CNPJ inválido'])

		# Sempre retorne a coleção completa de dados válidos.
		return cleaned_data