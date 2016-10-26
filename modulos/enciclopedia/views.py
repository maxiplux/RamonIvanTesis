from django.shortcuts import render, get_object_or_404

# Create your views here.


from django.http import Http404, HttpResponse
from django.shortcuts import render
from modulos.enciclopedia.models import Portada, Categoria, Articulo


def portada(request, pk):
    portada=get_object_or_404(Portada,pk=pk)
    image_data = open(portada.archivo.path, "rb").read()
    return HttpResponse(image_data, mimetype="image/png")

def indice(request):
    categorias=Categoria.objects.filter(primaria=True).order_by("-orden")
    data={'categorias':categorias}
    return render(request, 'modulos/enciclopedia/indice.html', data)


def contenido(request,pk):
    articulo=get_object_or_404(Articulo,pk=pk)
    categorias=Categoria.objects.filter(primaria=True).order_by("-orden")


    data={'articulo_detalle':articulo,'categorias':categorias}
    return render(request, 'modulos/enciclopedia/contenido.html', data)