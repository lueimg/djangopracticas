from django.contrib import admin

# Register your models here.
# usar .es importe relativo  , ya que track model esta en la misma carpeta
from .models import Track

class TrackAdmin(admin.ModelAdmin):
	#aumenta columnas en el admin de este contenido
	list_display = ('title','artist','order', 'album','player', 'es_pharrel')
	
	#para filtar en el admin por tipo de contenido
	list_filter = ('artist','album')

	#AGREGA UN BUSCADOR A LA CLASE
	search_fields = ('title','artist__firt_name','artist__last_name')


	def es_pharrel(self,obj):
		return obj.id == 1


	es_pharrel.boolean = True

# agrega el modelo y la clase de configuracion
admin.site.register(Track , TrackAdmin)