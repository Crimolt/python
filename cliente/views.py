#coding: utf-8
from django.shortcuts import render, get_object_or_404
from cliente.forms import ClienteForm
from endereco.forms import EnderecoForm
from cliente.models import Cliente

template_novo = 'cliente/novo.html'
template_detalhe = 'cliente/detalhe.html'
template_lista = 'cliente/lista.html'

def novo(request):
    dados = {}
    dados['form'] = ClienteForm()
    dados['formEndereco'] = EnderecoForm()
    dados['aux'] = '<script> alert("Levi is awesome") </script>'
    return render(request, template_novo, dados)

def salvar(request, id=None):
    dados = {}

    form = ClienteForm(request.POST or None)
    formEndereco = EnderecoForm(request.POST or None)

    if form.is_valid() and formEndereco.is_valid():
        cliente = form.save(commit=False)

        if id not in (None, '0'):
            cliente.id = id

        cliente.endereco = formEndereco.save()

        cliente.save()
        mensagem = 'Cliente salvo com sucesso!'
        return lista(request)
    else:
        dados['form'] = form
        dados['formEndereco'] = formEndereco
        dados['erros'] = form.errors
        dados['errosEnd'] = formEndereco.errors
        return render(request, template_novo, dados)


def detalhe(request, id, mensagem=None):
    dados = {}
    dados['mensagem'] = mensagem
    cliente = get_object_or_404(Cliente, id=id)
    form = ClienteForm(instance=cliente)
    dados['form'] = form
    dados['formEndereco'] = EnderecoForm(instance=cliente.endereco)
    dados['cliente'] = cliente
    return render(request, template_detalhe, dados)

def lista(request):
    dados = {}
    clientes = Cliente.objects.all()
    dados['clientes'] = clientes    
    return render(request, template_lista, dados)    