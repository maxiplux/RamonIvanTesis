__author__ = 'franc'

from django.conf.urls import patterns, url



from modulos.enciclopedia.views import indice,portada,contenido

urlpatterns = patterns('',
                       url(r'^$',indice, name='indice2'),
                       url(r'^(?P<pk>\d+)/$', portada, name='portada'),
                       url(r'^indice/$',indice, name='indice'),
                       url(r'^contenido/(?P<pk>\d+)/$',contenido, name='contenido'),

                       )