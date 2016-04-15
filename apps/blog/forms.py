from django import forms

from ..accounts.models import User

from .models import Topic, Post, TopicMessage, Moderated, Tag


class TopicForm(forms.ModelForm):
	tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all())
	class Meta:
		model = Topic
		fields = ['title', 'description', 'tags']


class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ['message']


class ModeratedForm(forms.ModelForm):
	class Meta:
		model = Moderated
		fields = ['text']

class PersonalMessageForm(forms.ModelForm):
	class Meta:
		model = TopicMessage
		fields = ['message']