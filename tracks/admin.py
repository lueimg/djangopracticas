from django.contrib import admin

# Register your models here.
# usar .es importe relativo  , ya que track model esta en la misma carpeta
from .models import Track

class TrackAdmin(admin.ModelAdmin):
	#aumenta columnas en el admin de este contenido
	list_display = ('title','artist','order', 'track_file','album')

# agrega el modelo y la clase de configuracion
admin.site.register(Track , TrackAdmin)