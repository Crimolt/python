#coding: utf-8
from django.conf.urls import patterns, include, url

urlpatterns = patterns('funcionario.views',    
    url(r'^novo$', 'novo', name='app_funcionario_novo'),
    url(r'^salvar/(?P<id>\d+)/$', 'salvar', name='app_funcionario_salvar'),
    url(r'^detalhe/(?P<id>\d+)/$', 'detalhe', name='app_funcionario_detalhe'),
)