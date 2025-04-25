from django.contrib import admin


from .models import Remixer
# from .models import   para extraer todo *

# root
# 1234


# Clase para personalizar la presentación de Remixer en el admin

class RemixerAdmin(admin.ModelAdmin):
    list_display = ('nombre_artistico', 'Track', 'Remixer', 'genero_musical',
                    'bpm', 'soundcloud')  # Añade 'soundcloud' como columna
    search_fields = ('nombre_artistico', 'Track', 'Remixer', 'genero_musical')
    list_filter = ('genero_musical', 'bpm')


# Register your models here.
admin.site.register(Remixer, RemixerAdmin)

title = "DjMax | Remixes"
sub_title = "Administración de Remixes"


admin.site.site_header = title
admin.site.index_title = sub_title
