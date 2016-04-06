from .models import ProgrammingLang, Topic, Post


def categories(request):
	context = {}
	context['categories'] = ProgrammingLang.objects.all()
	return context


def topics(requets):
	context = {}
	context['topics'] = Topic.objects.count()
	return context


def posts(requets):
	context = {}
	context['posts'] = Post.objects.count()
	return context