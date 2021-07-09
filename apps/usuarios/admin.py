from django.contrib import admin
from .models import Usuario

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ['nome', 'email', 'password_hash']

admin.site.register(Usuario, UsuarioAdmin)
