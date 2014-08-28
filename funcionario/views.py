#coding: utf-8
from django.shortcuts import render, get_object_or_404
from funcionario.forms import FuncionarioForm, AgenteForm, LiderForm
from endereco.forms import EnderecoForm
from funcionario.models import Funcionario
from django.http import HttpResponse

template_novo = 'funcionario/novo.html'
template_detalhe = 'funcionario/detalhe.html'
template_lista = 'funcionario/lista.html'

def novo(request):
    dados = {}
    dados['form'] = FuncionarioForm()
    dados['formEndereco'] = EnderecoForm()
    return render(request, template_novo, dados)

def novoLider(request):
    dados = {}
    dados['form'] = LiderForm()
    dados['formEndereco'] = EnderecoForm()
    return render(request, template_novo, dados)

def novoAgente(request):
    dados = {}
    dados['form'] = AgenteForm()
    dados['formEndereco'] = EnderecoForm()
    return render(request, template_novo, dados)    

def salvar(request, id=None):    
    dados = {}
    if request.POST['tipo_funcionario'] == 'L':
        form = LiderForm(request.POST or None)
    else:
        form = AgenteForm(request.POST or None)

    formEndereco = EnderecoForm(request.POST or None)

    if form.is_valid() and formEndereco.is_valid():
        funcionario = form.save(commit=False)

        if id not in (None, '0'):
            funcionario.id = id

        funcionario.endereco = formEndereco.save()

        funcionario.save()
        mensagem = 'Funcionario salvo com sucesso!'
        return detalhe(request, funcionario.id, mensagem)
    else:
        dados['form'] = form
        dados['formEndereco'] = formEndereco
        dados['erros'] = form.errors
        dados['errosEnd'] = formEndereco.errors
        return render(request, template_novo, dados)


def detalhe(request, id, mensagem=None):
	dados = {}
	dados['mensagem'] = mensagem
	funcionario = get_object_or_404(Funcionario, id=id)
	form = FuncionarioForm(instance=funcionario)
	dados['form'] = form
	dados['formEndereco'] = EnderecoForm(instance=funcionario.endereco)
	dados['funcionario'] = funcionario
	return render(request, template_detalhe, dados)

def lista(request):
    dados = {}
    funcionarios = Funcionario.objects.all()
    dados['funcionarios'] = funcionarios
    return render(request, template_lista, dados)        