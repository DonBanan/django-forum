from django.conf.urls import url

from . import views


urlpatterns = [
	url(r'^chat-form/$', views.chat_form, name='chat_form'),
]