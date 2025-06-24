from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render

# importar las clases de models.py
from ordenamiento.models import *

# Create your views here.

def index(request):
    # return HttpResponse("Hola mundo desde Python")
    return HttpResponse("Hola mundo desde Python en UTPL<br/><br/>%s" % (request.path))

def listadoParroquias(request):
    """
    Listar los registros del modelo Estudiante,
    obtenidos de la base de datos.
    """
    # a través del ORM de django se obtiene
    # los registros de la entidad; el listado obtenido
    # se lo almacena en una variable llamada
    # estudiantes
    parroquias = Parroquia.objects.all()
    barrios = Barrio.objects.all()
    # en la variable tipo diccionario llamada informacion_template
    # se agregará la información que estará disponible
    # en el template
    titulo = "Listado de Parroquias y Barrios"
    informacion_template = {'parroquias': parroquias,
    'numero_parroquias': len(parroquias),
    'Barrios': barrios}
    return render(request, 'listadoParroquia.html', informacion_template)


def listadoBarrios(request):

    barrios = Barrio.objects.all()

    informacion_template = {'barrios': barrios,
    'numero_barrios': len(barrios)}
    return render(request, 'listadoBarrios.html', informacion_template)
