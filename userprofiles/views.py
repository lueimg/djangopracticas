from django.shortcuts import render
from .forms import UserCreationEmailForm, EmailAuthenticationForm
from django.contrib.auth import login

def signup(request):
	# request.POST or None valida si se esta recibiendo post para llenar el formualrio o no 
	form = UserCreationEmailForm(request.POST or None)

	if form.is_valid():
		form.save()

	return render(request, "signup.html",{"form":form})

def signin(request):
	form = EmailAuthenticationForm(request.POST or None)

	if form.is_valid():
		
		login(request, form.get_user())

	return render(request, 'signin.html', {'form':form})

