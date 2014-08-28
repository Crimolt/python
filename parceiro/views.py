#coding: utf-8
from django.shortcuts import render, get_object_or_404
from parceiro.forms import ParceiroForm
from endereco.forms import EnderecoForm
from parceiro.models import Parceiro

template_novo = 'parceiro/novo.html'
template_detalhe = 'parceiro/detalhe.html'
template_lista = 'parceiro/lista.html'

def novo(request):
    dados = {}
    dados['form'] = ParceiroForm()
    dados['formEndereco'] = EnderecoForm()
    return render(request, template_novo, dados)

def salvar(request, id=None):
    dados = {}

    form = ParceiroForm(request.POST or None)
    formEndereco = EnderecoForm(request.POST or None)

    if form.is_valid() and formEndereco.is_valid():
        parceiro = form.save(commit=False)

        if id not in (None, '0'):
            parceiro.id = id

        parceiro.endereco = formEndereco.save()

        parceiro.save()
        mensagem = 'Parceiro salvo com sucesso!'
        return detalhe(request, parceiro.id, mensagem)


def detalhe(request, id, mensagem=None):
	dados = {}
	dados['mensagem'] = mensagem
	parceiro = get_object_or_404(Parceiro, id=id)
	form = ParceiroForm(instance=parceiro)
	dados['form'] = form
	dados['formEndereco'] = EnderecoForm(instance=parceiro.endereco)
	dados['parceiro'] = parceiro
	return render(request, template_detalhe, dados)

def lista(request):
    dados = {}
    #parceiros = Parceiro.objects.all()
    #dados['parceiros'] = parceiros
    return render(request, template_lista, dados)