from django.db import models

# Create your models here.
class Artist(models.Model):
	""" CharField es un input"""
	firt_name = models.CharField(max_length=255)
	""" Se usa blank = True  para que no sea un campo obligatorio"""
	last_name = models.CharField(max_length=255,blank=True)
	# TextField es una textarea
	biography = models.TextField(blank=True)

	favorite_songs = models.ManyToManyField('tracks.Track',blank=True,related_name='is_favorite_of')
	""" para syncronizar este campo a la bd 
	./manage.py schemamigration --auto artists
	 1636  ./manage.py schemamigration --initial artists
	 1637  ./manage.py migrate artists --fake
	 1638  ./manage.py schemamigration --auto artists
	 1639  ./manage.py migrate artists
	"""
	def __unicode__(self):
		return self.firt_name

	def es_pharrel(self):
		return self.id == 1
