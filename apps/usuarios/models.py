from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=220)
    email = models.EmailField()
    password_hash = models.CharField(max_length=220)
    
    @property
    def password():
        raise AttributeError("")

    

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"
        ordering = ['nome']