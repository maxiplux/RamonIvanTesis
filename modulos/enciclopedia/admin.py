from django.contrib import admin

# Register your models here.
from modulos.enciclopedia.models import clases, Articulo, Imagen
from modulos.utilidades.utiladmin import GenerateAdmins



class ImageInline(admin.StackedInline):
    model = Imagen


class ArticuloAdmin(admin.ModelAdmin):

    list_display=["id"]+Articulo.GetFieldsAdmin()
    filtros=Articulo.GetFieldsAdmin()
    search_fields=['titulo','categoria__nombre']
    #list_editable = ['activo']
    list_filter=['categoria']
    inlines = [ ImageInline, ]



GenerateAdmins(clases())


admin.site.register(Articulo, ArticuloAdmin)