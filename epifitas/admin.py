from django.contrib import admin
from .models import (Especie, InfoGeografica, InfoReproducao, Foto)


class EspecieAdmin(admin.ModelAdmin):
    list_display = ['id', 'sinonimia', 'genero',
                    'epiteto', 'familia', 'link_flora', 'ativa']


class InfoGeograficaAdmin(admin.ModelAdmin):
    list_display = ['id', 'especie', 'numero_registros',
                    'longitude', 'latitude']


class InfoReproducaoAdmin(admin.ModelAdmin):
    list_display = ['id', 'especie', 'flor', 'info_flor',
                    'fruto', 'info_fruto', 'antese',
                    'tipo_reproducao', 'recursos_oferecidos',
                    'semente', 'info_semente', 'info_botanica']


class FotoAdmin(admin.ModelAdmin):
    list_display = ['id', 'especie', 'planta', 'fruto', 'flor', 'folha']


admin.site.register(Especie, EspecieAdmin)
admin.site.register(InfoGeografica, InfoGeograficaAdmin)
admin.site.register(InfoReproducao, InfoReproducaoAdmin)
admin.site.register(Foto, FotoAdmin)
