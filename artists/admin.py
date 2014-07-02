from django.contrib import admin

# Register your models here.
from .models import Artist

#vamos a editar los tracks desde el modelo artist
from tracks.models import Track

## para manejar edicion de datos relaciones e nla misma liena
class TrackInline(admin.StackedInline):
	model = Track
	extra = 1 # campos vacios extras para agregar mas tracks  a los artistas

from albums.models import Album

class AlbumInline(admin.StackedInline):
	model = Album
	extra = 1


class ArtistAdmin(admin.ModelAdmin):

	search_fields = ('firt_name','last_name')

	inlines = [AlbumInline,TrackInline,] #clases de modelos a relacionar para editar 




admin.site.register(Artist,ArtistAdmin)