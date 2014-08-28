#coding: utf-8
from django import forms
from funcionario.models import Funcionario
from pessoa.forms import PessoaForm
    
class FuncionarioForm(PessoaForm):
    class Meta:
        model = Funcionario
        exclude = ['endereco']

class AgenteForm(FuncionarioForm):
	lider = forms.ModelChoiceField(queryset=Funcionario.objects.filter(tipo_funcionario='L'))
	tipo_funcionario = forms.CharField(widget=forms.HiddenInput(), initial='A')
	class Meta:
		model = Funcionario
		exclude = ['endereco', ]

class LiderForm(FuncionarioForm):
	tipo_funcionario = forms.CharField(widget=forms.HiddenInput(), initial='L')
	class Meta:
		model = Funcionario
		exclude = ['endereco', 'tipo_funcionario', 'lider']
