#coding: utf-8
from django.db import models
from pessoa.models import Pessoa

TIPO_FUNCIONARIO = (
	('A', u'Agente'),
	('L', u'Lider'),
)

class Funcionario(Pessoa):
	data_admicao = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True, verbose_name='Data de Admição')
	tipo_funcionario = models.CharField(max_length=1, null=False, blank=False, choices=TIPO_FUNCIONARIO, default='A', verbose_name='Tipo')
	lider = models.ForeignKey('self', null=True, blank=True, related_name='lider_funcionario')