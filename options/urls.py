from django.conf.urls import url

from . import views
app_name = 'options'

urlpatterns = [

    # ex: /pru/
     url(r'^$', views.index, name='index'),
     url(r'^mapa', views.mapa, name='mapa'),

    # ex: /localizaciones/
   #  url(r'^$', views.index, name='index'),
    # ex: /localizaciones/index
  #   url(r'^index2/$', views.index2, name='index2'),
    # ex: /localizaciones/5/
  #   url(r'^(?P<localizacion_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /localizaciones/5/results/
  #   url(r'^(?P<localizacion_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /datos/localizaciones/5/
 #    url(r'^datos/(?P<localizacion_id>[0-9]+)/$', views.datos, name='datos'),
    # ex: /datos/localizaciones/5/resultados/
 #    url(r'^datos/(?P<localizacion_id>[0-9]+)/resultados/$', views.resultados, name='resultados'),
    # ex: /mapa/localizaciones/5/resultados/
   ## url(r'^mapa/$', views.mapa, name='mapa'),
  #   url(r'^pru2/$', views.pru2, name='pru2'),
 #    url(r'^mapa(?P<localizacion_id>[0-9]+)/$', views.mapa, name='mapa'),

]
