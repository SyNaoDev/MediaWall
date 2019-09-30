from django.shortcuts import render, redirect
from django.contrib import sessions, messages

import bcrypt

from .models import User

def user_valid(request):
	if 'MEDIA_WALL_AUTH' in request.session:
		value = request.session['MEDIA_WALL_AUTH']
		return value != 0
	return False

def index(request):
	return render(request, 'index.html')

def login(request):
	email = request.POST['email']
	users = User.objects.filter(email=email)
	if len(users) != 0:
		user = users[0]
		if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
			request.session['MEDIA_WALL_AUTH'] = user.id
			return redirect('/wall')
	errors = {
		'login': 'Either email or password was incorrect!'
	}
	messages.error(request, errors)
	return redirect('/auth')

def logout(request):
	request.session['MEDIA_WALL_AUTH'] = 0
	return redirect('/auth')

def register(request):
	errors = User.objects.verify_info(request.POST)
	if len(errors) > 0:
		messages.error(request, errors)
		return redirect('/auth')
	hashed_password = bcrypt.hashpw(
		request.POST['password'].encode(),
		bcrypt.gensalt()
	)
	user = User.objects.create(
		first_name=request.POST['first_name'],
		last_name=request.POST['last_name'],
		email=request.POST['email'],
		password=hashed_password.decode('utf-8')
	)
	request.session['MEDIA_WALL_AUTH'] = user.id
	return redirect('/wall')
