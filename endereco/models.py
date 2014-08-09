from django.db import models

TIPO_LOGRADOURO = (
    ('RUA', u'Rua'),
    ('AVENIDA', u'Avenida')
    )

class Endereco(models.Model):
    tipo_logradouro = models.CharField(max_length=20, choices=TIPO_LOGRADOURO, default='RUA', null=False, blank=False)
    logradouro = models.CharField(max_length=60, null=False, blank=False)
    numero = models.IntegerField(null=False, blank=False)
    bairro = models.CharField(max_length=60, null=False, blank=False)
    cidade = models.CharField(max_length=60, null=False, blank=False)
    uf = models.CharField(max_length=2, null=False, blank=False)
    cep = models.CharField(max_length=8, null=False, blank=False)