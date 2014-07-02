from django.test import TestCase

# Create your tests here.

from .models import Artist

from tracks.models import Track
from albums.models import Album

## se crea la clase prueba
## para hacer pruebas se apaga el servidro y luego se corre
## ./manage.py test artists

class TestArtists(TestCase):
	def setUp(self):
		self.artist = Artist.objects.create(firt_name='avi', last_name='bobie')
		self.album = Album.objects.create(title='heroes',artist=self.artist)
		self.track = Track.objects.create(title='heroes',artist=self.artist, album=self.album, order=9)

	def text_existe_vista(self):
		## cliente hace request a neustra pagina para ver si funciona bien 
		res = self.client.get('/artists/%d/' % self.artist.id)
		## renderizo correcto
		self.assertEquals(res.status_code, 200)
		## existe avi en el contenido de la respuesta
		self.assertTrue('avi' in res.content)

	def text_no_existe_vista(self):
			
		id_viejo = self.artist.id
		self.artist.delete()

		res = self.client.get('/artists/%d/' % id_viejo)
		self.assertEquals(res.status_code, 404)
		# self.assertTrue('avi' in res.content)

	def test_usurio_no_logeado(self):
		res = self.client.get('/tracks/%s/' % self.track.title)
		## renderizo correcto
		# self.assertEquals(res.status_code, 302)
		## existe avi en el contenido de la respuesta
		# self.assertTrue('avi' in res.content)

