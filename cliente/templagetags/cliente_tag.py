from django import template
from cliente.models import TIPO_PESSOA

register = template.Library()

@register.filter
def quality(q):
    for choice in TIPO_PESSOA:
        if choice[0] == q:
            return choice[1]
    return ''