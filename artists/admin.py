from django.contrib import admin

# Register your models here.
from .models import Artist


class ArtistAdmin(admin.ModelAdmin):

	search_fields = ('firt_name','last_name')



admin.site.register(Artist,ArtistAdmin)