#coding: utf-8
from django.conf.urls import patterns, include, url

urlpatterns = patterns('cliente.views',    
    url(r'^novo/$', 'novo', name='app_cliente_novo'),
    url(r'^salvar/(?P<id>\d+)/$', 'salvar', name='app_cliente_salvar'),
    url(r'^detalhe/(?P<id>\d+)/$', 'detalhe', name='app_cliente_detalhe'),
    url(r'^lista/$', 'lista', name='app_cliente_lista'),
)