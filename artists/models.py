from django.db import models

# Create your models here.
class Artist(models.Model):
	""" CharField es un input"""
	firt_name = models.CharField(max_length=255)
	""" Se usa blank = True  para que no sea un campo obligatorio"""
	last_name = models.CharField(max_length=255,blank=True)
	# TextField es una textarea
	biography = models.TextField(blank=True)

	def __unicode__(self):
		return self.firt_name
