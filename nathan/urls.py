#coding: utf-8
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^cliente/', include('cliente.urls')),
)

urlpatterns += patterns('',
    url(r'^parceiro/', include('parceiro.urls')),
)

urlpatterns += patterns('',
    url(r'^funcionario/', include('funcionario.urls')),
)

urlpatterns += patterns('',
    # Examples:
    # url(r'^$', 'nathan.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'core.views.home', name='home'),
)
