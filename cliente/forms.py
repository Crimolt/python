#coding: utf-8
from django import forms
from pessoa.forms import PessoaForm
from cliente.models import Cliente

class ClienteForm(PessoaForm):
	class Meta:
		model = Cliente
		exclude = ['endereco']
		read_only = ['data_cadastro']