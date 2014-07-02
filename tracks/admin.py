from django.contrib import admin

# Register your models here.
# usar .es importe relativo  , ya que track model esta en la misma carpeta
from .models import Track

class TrackAdmin(admin.ModelAdmin):
	#aumenta columnas en el admin de este contenido
	list_display = ('title','artist','order', 'track_file','album')
	
	#para filtar en el admin por tipo de contenido
	list_filter = ('artist','album')

	#AGREGA UN BUSCADOR A LA CLASE
	search_fields = ('title','artist__firt_name','artist__last_name')






# agrega el modelo y la clase de configuracion
admin.site.register(Track , TrackAdmin)