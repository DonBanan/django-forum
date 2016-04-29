from django.db.models import Count
from .models import Category, Topic, Post, Tag


def categories(request):
	context = {}
	context['categories'] = Category.objects.all()
	return context


def topics(requets):
	context = {}
	context['topics'] = Topic.objects.count()
	return context


def posts(requets):
	context = {}
	context['posts'] = Post.objects.count()
	return context


def tags(request):
	context = {}
	context['tags'] = Tag.objects.all().annotate(num_topic=Count('topic_tags')).order_by('-num_topic')
	return context