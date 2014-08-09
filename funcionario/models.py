from django.db import models
from pessoa.models import Pessoa

class Funcionario(Pessoa):
	data_admicao = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True, verbose_name="Data de Admção")