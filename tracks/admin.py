from django.contrib import admin

# Register your models here.
# usar .es importe relativo  , ya que track model esta en la misma carpeta
from .models import Track

admin.site.register(Track)