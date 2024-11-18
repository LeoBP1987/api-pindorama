from django.contrib import admin
from pindorama.models import Tipos, Formas, Origens, Criaturas, AlbumCriaturas, LendasCriaturas, EtiquetasCriaturas, Elementos

class TiposAdmin(admin.ModelAdmin):
    list_display = ('tipo', 'data_criacao')
    list_display_links = ('tipo',)
    list_per_page = 10
    search_fields = ('tipo', 'data_criacao')
    ordering = ('tipo',)

admin.site.register(Tipos, TiposAdmin)

class FormasAdmin(admin.ModelAdmin):
    list_display = ('forma', 'data_criacao')
    list_display_links = ('forma',)
    list_per_page = 10
    search_fields = ('forma', 'data_criacao')
    ordering = ('forma',)

admin.site.register(Formas, FormasAdmin)

class OrigensAdmin(admin.ModelAdmin):
    list_display = ('origem', 'data_criacao')
    list_display_links = ('origem',)
    list_per_page = 10
    search_fields = ('origem', 'data_criacao')
    ordering = ('origem',)

admin.site.register(Origens, OrigensAdmin)

class CriaturasAdmin(admin.ModelAdmin):
    list_display = ('criatura', 'tipo', 'forma', 'origem', 'modo', 'data_criacao')
    list_display_links = ('criatura', 'data_criacao', 'modo', )
    list_per_page = 10
    search_fields = ('criatura', 'tipo', 'forma', 'origem', 'modo', 'data_criacao')
    ordering = ('criatura',)

admin.site.register(Criaturas, CriaturasAdmin)

class EtiquetasCriaturasAdmin(admin.ModelAdmin):
    list_display = ('criatura', 'etiqueta')
    list_display_links = ('criatura', 'etiqueta')
    list_per_page = 10
    search_fields = ('criatura', 'etiqueta')
    ordering = ('criatura',)

admin.site.register(EtiquetasCriaturas, EtiquetasCriaturasAdmin)

class AlbumCriaturasAdmin(admin.ModelAdmin):
    list_display = ('criatura', 'fonte', 'data_criacao')
    list_display_links = ('criatura', 'fonte', 'data_criacao')
    list_per_page = 10
    search_fields = ('criatura', 'fonte', 'data_criacao')
    ordering = ('criatura',)

admin.site.register(AlbumCriaturas, AlbumCriaturasAdmin)

class LendasCriaturasAdmin(admin.ModelAdmin):
    list_display = ('criatura', 'fonte', 'estoria', 'titulo', 'data_criacao')
    list_display_links = ('criatura', 'titulo', 'fonte', 'data_criacao')
    list_per_page = 10
    search_fields = ('criatura', 'titulo', 'fonte', 'data_criacao')
    ordering = ('titulo',)

admin.site.register(LendasCriaturas, LendasCriaturasAdmin)

class ElementosAdmin(admin.ModelAdmin):
    list_display = ('elemento', 'tipo', 'data_criacao')
    list_display_links = ('elemento', 'tipo')
    list_per_page = 10
    search_fields = ('elemento', 'tipo')
    ordering = ('elemento',)

admin.site.register(Elementos, ElementosAdmin)