from __future__ import unicode_literals
import pyclbr
from tinymce.models import HTMLField
from django.db import models

# Create your models here.
from modulos.maestras.models import Maestra, MaestraSimple
from autoslug import AutoSlugField


class Portada(Maestra):


    archivo = models.ImageField(upload_to='portada')

    def __unicode__(self):
        return u'%s' % self.nombre


    class Meta(Maestra.Meta):
        verbose_name = u"Portada"
        verbose_name_plural = u"Portadas"
        ordering = ['nombre']

class Categoria(Maestra):
    sub_categoria=models.ForeignKey('self',null=True,blank=True)
    def __unicode__(self):
        if self.sub_categoria:
            return u'%s / %s' % (self.sub_categoria.nombre,self.nombre)
        return u'%s ' % self.nombre

    @property
    def articulos(self):
        return Articulo.objects.filter(categoria=self)

    class Meta(Maestra.Meta):
        verbose_name = u"Categoria"
        verbose_name_plural = u"Categorias"
        ordering = ['nombre']


class Articulo(MaestraSimple):
    categoria=models.ForeignKey(Categoria)
    titulo = models.CharField(max_length=255, blank=True, unique=True)
    slug = AutoSlugField(populate_from='titulo', unique=True)


    resumen=HTMLField(null=True,blank=True)
    contenido=HTMLField()


    def __unicode__(self):
        return u'%s/%s' % (self.categoria.nombre,self.titulo)

    class Meta(Maestra.Meta):
        verbose_name = u"Articulo"
        verbose_name_plural = u"Articulos"
        ordering = ['titulo']

    @property
    def imagenes(self):
        return Imagen.objects.filter(articulo=self)







class Imagen(MaestraSimple):
    archivo = models.ImageField(upload_to='articulos/imagenes/')
    articulo=models.ForeignKey(Articulo)


def clases():
    for clase in pyclbr.readmodule(__name__).keys():
        if clase not in ['Imagen','Articulo']:
            yield eval(clase)


#python manage.py loadtestdata enciclopedia.Categoria:5 enciclopedia.Articulo:20 enciclopedia.Imagen:20