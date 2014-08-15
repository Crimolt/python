#coding: utf-8
from django.db import models
from endereco.models import Endereco

TIPO_PESSOA = (
    ('F', u'FÍSICA'),
    ('J', u'JURÍDICA'),
)

class Pessoa(models.Model):
    nome = models.CharField(max_length=60, null=False, blank=False)
    nome_fantasia = models.CharField(max_length=60, null=True, blank=True, verbose_name = u'Nome Fantasia')
    tipo_pessoa = models.CharField(max_length=1, choices=TIPO_PESSOA, default='F', null=False, blank=False, verbose_name = u'Tipo')
    cpf = models.CharField(max_length=20, null=True, blank=True)
    rg = models.CharField(max_length=20, null=True, blank=True)
    cnpj = models.CharField(max_length=20, null=True, blank=True)
    inscricao_estadual = models.CharField(max_length=20, null=True, blank=True, verbose_name = u'Inscrição Etadual')
    inscricao_municipal = models.CharField(max_length=20, null=True, blank=True)
    endereco = models.ForeignKey(Endereco, null = False, blank = False, related_name = 'endereco_cli')
    telefone = models.CharField(max_length=20, null=True, blank=True)
    celular = models.CharField(max_length=20, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    data_cadastro = models.DateTimeField(null=True, blank=True, verbose_name="Data de Cadastro")