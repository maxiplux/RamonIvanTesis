from django.contrib import admin

# Register your models here.
from modulos.enciclopedia.models import clases, Articulo, Imagen, Categoria
from modulos.utilidades.utiladmin import GenerateAdmins




class ImageInline(admin.TabularInline):
    model = Imagen

class CategoriaInline(admin.TabularInline):
    model = Categoria




class ArticuloAdmin(admin.ModelAdmin):

    list_display=["id"]+Articulo.GetFieldsAdmin()
    filtros=Articulo.GetFieldsAdmin()
    search_fields=['titulo','categoria__nombre']
    #list_editable = ['activo']
    list_filter=['categoria']
    inlines = [ ImageInline, ]


class CategoriaAdmin(admin.ModelAdmin):

    list_display=["id"]+Categoria.GetFieldsAdmin()
    filtros=Categoria.GetFieldsAdmin()
    list_editable = ['orden']
    search_fields=['nombre']
    #list_editable = ['activo']
    list_filter=['categoria']
    inlines = [ CategoriaInline, ]


GenerateAdmins(clases())


admin.site.register(Articulo, ArticuloAdmin)
admin.site.register(Categoria, CategoriaAdmin)