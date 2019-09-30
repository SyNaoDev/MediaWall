from __future__ import unicode_literals
from django.db import models

class UserManager(models.Manager):
	def verify_info(self, post_info):
		errors = {}
		if len(post_info['first_name']) < 3:
			errors['first_name'] = 'First Name must be at least 3 characters'
		if len(post_info['last_name']) < 3:
			errors['last_name'] = 'Last Name must be at least 3 characters'
		if not '@' in post_info['email']:
			errors['email'] = 'Email address is invalid'
		if len(User.objects.filter(email=post_info['email'])) > 1:
			errors['already'] = 'Account with that email already exists'
		if len(post_info['password']) < 8:
			errors['password'] = 'Password must be at least 8 characters'
		if post_info['password'] != post_info['password_confirm']:
			errors['password_confirm'] = 'Passwords must match'
		return errors

class User(models.Model):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	email = models.CharField(max_length=100)
	password = models.CharField(max_length=100)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = UserManager()
