from __future__ import unicode_literals
from django.db import models

from app_auth.models import User

class WallMessage(models.Model):
	user = models.ForeignKey(User, related_name="messages", on_delete=models.CASCADE)
	text = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class WallComment(models.Model):
	message = models.ForeignKey(WallMessage, related_name="comments", on_delete=models.CASCADE)
	user = models.ForeignKey(User, related_name="comments", on_delete=models.CASCADE)
	text = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
