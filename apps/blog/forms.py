from django import forms

from ..accounts.models import User

from .models import Topic, Post, PersonalMessage


class TopicForm(forms.ModelForm):
	class Meta:
		model = Topic
		fields = ['title', 'description', 'tags']


class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ['message']


class PersonalMessageForm(forms.ModelForm):
	class Meta:
		model = PersonalMessage
		fields = ['message']