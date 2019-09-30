from django.shortcuts import render, redirect
from django.contrib import sessions

from .models import WallMessage, WallComment, User

def user_valid(request):
	if 'MEDIA_WALL_AUTH' in request.session:
		value = request.session['MEDIA_WALL_AUTH']
		return value != 0
	return False

def index(request):
	if not user_valid(request):
		return redirect('/auth')
	user_id = request.session['MEDIA_WALL_AUTH']
	context = {
		'user': User.objects.get(id=user_id),
		'wall_msgs': WallMessage.objects.all().order_by('-created_at')
	}
	return render(
		request, 
		'home.html', 
		context
	)

def post_message(request, user_id):
	WallMessage.objects.create(
		user=User.objects.get(id=user_id),
		text=request.POST['text']
	)
	return redirect('/wall')

def post_comment(request, user_id, message_id):
	user = User.objects.get(id=user_id)
	message = WallMessage.objects.get(id=message_id)
	WallComment.objects.create(
		user=user,
		message=message,
		text=request.POST['text']
	)
	return redirect('/wall')

def remove_message(request, message_id):
	message = WallMessage.objects.get(id=message_id)
	message.delete()
	return redirect('/wall')