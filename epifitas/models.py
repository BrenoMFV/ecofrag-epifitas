from django.db import models
from usuarios.models import CustomUser

class Especie(models.Model):
    sinonimia = models.CharField(max_length=220, db_index=True) # é isso mesmo?
    genero = models.CharField(max_length=220, db_index=True)
    epiteto = models.CharField(max_length=220, db_index=True)
    familia = models.CharField(max_length=220, db_index=True)
    link_flora = models.CharField(max_length=220, blank=True)
    ativa = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Espécie"
        verbose_name_plural = "Espécies"
        ordering = ['sinonimia']

    def __str__(self):
        return self.sinonimia


class InfoGeografica(models.Model):
    especie = models.ForeignKey(Especie, on_delete=models.CASCADE)
    numero_registros = models.IntegerField(db_index=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    
    class Meta:
        verbose_name = "Informação Geográfica"
        verbose_name_plural = "Informações Geográficas"
        ordering = ['especie']

    def __str__(self):
        return '{}, {}'.format(self.latitude, self.longitude)


class InfoReproducao(models.Model):
    TIPO_REPRODUCAO_CHOICES =[
        ('ND', 'Não Definido'),
        ('AUTO', 'Autogamia'),
        ('XENO', 'Xenogamia'), 
        ('HERCO', 'Hercogamia'),
    ]
    especie = models.ForeignKey(Especie, on_delete=models.CASCADE)
    flor = models.CharField(max_length=220)
    info_flor = models.TextField()
    fruto = models.CharField(max_length=220)
    info_fruto = models.CharField(max_length=220)
    antese = models.CharField(max_length=220) # wtf?
    tipo_reproducao = models.CharField(max_length=6, choices=TIPO_REPRODUCAO_CHOICES, default="ND")
    recursos_oferecidos = models.TextField()
    semente = models.CharField(max_length=220)
    info_semente = models.TextField()
    info_botanica = models.TextField()

    class Meta:
        verbose_name = "Informação Reprodutiva"
        verbose_name_plural = "Informações Reprodutivas"
        ordering = ['especie']

    def __str__(self):
        return f'{self.flor}, {self.fruto}, {self.semente}'


class Foto(models.Model):
    # /MEDIA_ROOT/<id>/<nome_do_campo>/
    def dir_fruto(instance, filename):
        return '{0}/fruto/{1}'.format(instance.especie.id, filename)
    
    def dir_flor(instance, filename):
        return '{0}/flor/{1}'.format(instance.especie.id, filename)
    
    def dir_folha(instance, filename):
        return '{0}/folha/{1}'.format(instance.especie.id, filename)
    
    def dir_planta(instance, filename):
         return '{0}/planta/{1}'.format(instance.especie.id, filename)

    especie = models.ForeignKey(Especie, on_delete=models.CASCADE)
    planta = models.FileField(upload_to=dir_planta, db_index=True, blank=True)
    fruto = models.FileField(upload_to=dir_fruto, db_index=True, blank=True)
    flor = models.FileField(upload_to=dir_flor, db_index=True, blank=True)
    folha = models.FileField(upload_to=dir_folha, db_index=True, blank=True)
    usuario = models.ForeignKey(CustomUser, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.planta}'

    