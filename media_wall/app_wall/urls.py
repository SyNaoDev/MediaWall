from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index),
	url(r'^message/(?P<user_id>\d+)$', views.post_message),
	url(r'^comment/(?P<user_id>\d+)/(?P<message_id>\d+)$', views.post_comment),
	url(r'^remove/(?P<message_id>\d+)$', views.remove_message)
]