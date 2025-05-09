# Generated by Django 5.0 on 2024-06-29 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Remixer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Track', models.CharField(max_length=100, verbose_name='Track')),
                ('nombre_artistico', models.CharField(max_length=100, unique=True, verbose_name='Nombre Artístico')),
                ('Remixer', models.CharField(max_length=100, verbose_name='Remixer')),
                ('genero_musical', models.CharField(max_length=50, verbose_name='Género Musical')),
                ('bpm', models.IntegerField(blank=True, null=True, verbose_name='BPM')),
                ('soundcloud', models.URLField(blank=True, null=True, verbose_name='SoundCloud')),
                ('foto_perfil', models.ImageField(blank=True, null=True, upload_to='remixers_profiles/', verbose_name='Fotografía')),
                ('pista_audio', models.FileField(blank=True, null=True, upload_to='remixers_audio/', verbose_name='Pista de audio')),
                ('enlace_descarga', models.URLField(blank=True, null=True, verbose_name='Enlace de descarga')),
                ('enlace_compra', models.URLField(blank=True, null=True, verbose_name='Enlace de compra')),
            ],
        ),
    ]
