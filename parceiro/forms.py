#coding: utf-8
from django import forms
from pessoa.forms import PessoaForm
from parceiro.models import Parceiro

class ParceiroForm(PessoaForm):
	class Meta:
		model = Parceiro
		exclude = ['endereco']
		read_only = ['data_cadastro']