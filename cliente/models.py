#coding: utf-8
from django.db import models
from pessoa.models import Pessoa

class Cliente(Pessoa):
	nome_mae = models.CharField(max_length=60, null=True, blank=True)
	nome_pai = models.CharField(max_length=60, null=True, blank=True)