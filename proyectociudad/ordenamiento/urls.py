from django.urls import path

from . import views


urlpatterns = [
        path('inicio', views.index, name='index'),
        path('listado/parroquias', views.listadoParroquias,
            name='listadoParroquias'),
        path('listado/barrios', views.listadoBarrios,
            name='listadoBarrios'),
 ]
