from .models import Category, Topic, Post


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