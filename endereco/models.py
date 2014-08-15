#coding: utf-8
from django.db import models

TIPO_LOGRADOURO = (
    ('RUA', u'Rua'),
    ('AVENIDA', u'Avenida')
)

class Endereco(models.Model):
    tipo_logradouro = models.CharField(max_length=20, choices=TIPO_LOGRADOURO, default='RUA', null=False, blank=False)
    logradouro = models.CharField(max_length=60, null=True, blank=True)
    numero = models.IntegerField(null=True, blank=True)
    bairro = models.CharField(max_length=60, null=True, blank=True)
    cidade = models.CharField(max_length=60, null=True, blank=True)
    uf = models.CharField(max_length=2, null=True, blank=True)
    cep = models.CharField(max_length=8, null=True, blank=True)