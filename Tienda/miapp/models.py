from django.db import models

# Create your models here.


class Remixer(models.Model):
    Track = models.CharField(max_length=100, verbose_name='Track')
    nombre_artistico = models.CharField(
        max_length=100, unique=True, verbose_name='Nombre Artístico')
    Remixer = models.CharField(max_length=100, verbose_name='Remixer')
    genero_musical = models.CharField(
        max_length=50, verbose_name='Género Musical')
    bpm = models.IntegerField(null=True, blank=True, verbose_name='BPM')
    soundcloud = models.URLField(
        blank=True, null=True, verbose_name='SoundCloud')
    foto_perfil = models.ImageField(
        upload_to='remixers_profiles/', blank=True, null=True, verbose_name='Fotografía')
    pista_audio = models.FileField(
        upload_to='remixers_audio/', blank=True, null=True, verbose_name='Pista de audio')
    enlace_descarga = models.URLField(
        blank=True, null=True, verbose_name='Enlace de descarga')
    enlace_compra = models.URLField(
        blank=True, null=True, verbose_name='Enlace de compra')

    def __str__(self):
        return self.nombre_artistico
