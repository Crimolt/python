from django.db import models
from pessoa.models import Pessoa

class Parceiro(Pessoa):
	data_inicio_parceria = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True, verbose_name="Data de Início da Parceria")
	validade_parceria = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True, verbose_name="Validade da Parceria")
	porcentagem_desconto = models.FloatField(null=True, blank=True, verbose_name="Porcentagem de Desconto")