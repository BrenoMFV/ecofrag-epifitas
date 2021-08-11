import uuid
from django.db import models
from django.urls import reverse
from users.models import CustomUser


class Especie(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    sinonimia = models.CharField(max_length=220)  # é isso mesmo?
    genero = models.CharField(max_length=220)
    epiteto = models.CharField(max_length=220)
    familia = models.CharField(max_length=220)
    link_flora = models.CharField(max_length=220)
    adicionada_em = models.DateTimeField(auto_now_add=True)
    ativa = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Espécie"
        verbose_name_plural = "Espécies"
        ordering = ['sinonimia']

    def __str__(self):
        return self.sinonimia

    def get_absolute_url(self):
        return reverse('epifita_detail', args=[str(self.id)])


class InfoGeografica(models.Model):
    especie = models.OneToOneField(Especie, on_delete=models.CASCADE)
    numero_registros = models.IntegerField()
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)

    class Meta:
        verbose_name = "Informação Geográfica"
        verbose_name_plural = "Informações Geográficas"
        ordering = ['especie']

    def __str__(self):
        return '{}, {}'.format(self.latitude, self.longitude)


class InfoReproducao(models.Model):
    TIPO_REPRODUCAO_CHOICES = [
        ('ND', 'Não Definido'),
        ('AUTO', 'Autogamia'),
        ('XENO', 'Xenogamia'),
        ('HERCO', 'Hercogamia'),
    ]
    especie = models.OneToOneField(Especie, on_delete=models.CASCADE)
    flor = models.CharField(max_length=220)
    info_flor = models.TextField()
    fruto = models.CharField(max_length=220)
    info_fruto = models.CharField(max_length=220)
    antese = models.CharField(max_length=220)  # wtf?
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
    especie = models.OneToOneField(Especie, on_delete=models.CASCADE)
    planta = models.ImageField(upload_to='plantas/', blank=True, null=True)
    fruto = models.ImageField(upload_to='frutos/', blank=True, null=True)
    flor = models.ImageField(upload_to='flores/', blank=True, null=True)
    folha = models.ImageField(upload_to='folhas/', blank=True, null=True)
    usuario = models.ForeignKey(CustomUser, on_delete=models.PROTECT, related_name='uploaded_by')

    def __str__(self):
        return f'{self.planta}'
