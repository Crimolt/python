from django.conf.urls import patterns, include, url

urlpatterns = patterns('parceiro.views',    
    url(r'^novo$', 'novo', name='app_parceiro_novo'),
    url(r'^salvar/(?P<id>\d+)/$', 'salvar', name='app_parceiro_salvar'),
    url(r'^detalhe/(?P<id>\d+)/$', 'detalhe', name='app_parceiro_detalhe'),
)