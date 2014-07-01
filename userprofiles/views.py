from django.shortcuts import render
from .forms import UserCreationEmailForm

def signup(request):
	# request.POST or None valida si se esta recibiendo post para llenar el formualrio o no 
	form = UserCreationEmailForm(request.POST or None)

	if form.is_valid():
		form.save()

	return render(request, "signup.html",{"form":form})
