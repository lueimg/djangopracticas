from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse, Http404

from .models import Track

import json
# Create your views here.
# @login_required me falta la calse de decoradores
def track_view(request, title):
	# try:
	# 	track = Track.objects.get(title=title)
	# except Track.DoesNotExist:
	# 	raise Http404
	# pip install ipdb
	# import ipdb; ipdb.set_trace() # pip install ipdb // aparecera automaticamente en el shell del server  , para salir ctrl + D

	track = get_object_or_404(Track , title=title)

	# return HttpResponse('Ok')
	return render(request,'track.html',{'track':track})

def track_view_json(request, title):

	track = get_object_or_404(Track , title=title)
	bio  = track.artist.biography
	data = {
		"title":track.title,
		"order":track.order,
		"album":track.album.title,
		"artist":{
			"name":track.artist.firt_name,
			"bio":bio
		}
	}

	json_data = json.dumps(data)

	return HttpResponse(json_data, content_type="application/json")


from rest_framework import viewsets

class TrackViewSet(viewsets.ModelViewSet):
	model = Track