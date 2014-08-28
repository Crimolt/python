#coding: utf-8
from django.conf.urls import patterns, include, url

urlpatterns = patterns('funcionario.views',    
    url(r'^novo$', 'novo', name='app_funcionario_novo'),
    url(r'^novoAgente$', 'novoAgente', name='app_funcionario_novoAgente'),
    url(r'^novoLider$', 'novoLider', name='app_funcionario_novoLider'),
    url(r'^salvar/(?P<id>\d+)/$', 'salvar', name='app_funcionario_salvar'),
    url(r'^detalhe/(?P<id>\d+)/$', 'detalhe', name='app_funcionario_detalhe'),
    url(r'^lista/$', 'lista', name='app_funcionario_lista'),
)