#coding: utf-8
from django.shortcuts import render, get_object_or_404
from funcionario.forms import FuncionarioForm
from endereco.forms import EnderecoForm
from funcionario.models import Funcionario

template_novo = 'funcionario/novo.html'
template_detalhe = 'funcionario/detalhe.html'

def novo(request):
    dados = {}
    dados['form'] = FuncionarioForm()
    dados['formEndereco'] = EnderecoForm()
    return render(request, template_novo, dados)

def salvar(request, id=None):
    dados = {}

    form = FuncionarioForm(request.POST or None)
    formEndereco = EnderecoForm(request.POST or None)

    if form.is_valid() and formEndereco.is_valid():
        funcionario = form.save(commit=False)

        if id not in (None, '0'):
            funcionario.id = id

        funcionario.endereco = formEndereco.save()

        funcionario.save()
        mensagem = 'Funcionario salvo com sucesso!'
        return detalhe(request, funcionario.id, mensagem)


def detalhe(request, id, mensagem=None):
	dados = {}
	dados['mensagem'] = mensagem
	funcionario = get_object_or_404(Funcionario, id=id)
	form = FuncionarioForm(instance=funcionario)
	dados['form'] = form
	dados['formEndereco'] = EnderecoForm(instance=funcionario.endereco)
	dados['funcionario'] = funcionario
	return render(request, template_detalhe, dados)