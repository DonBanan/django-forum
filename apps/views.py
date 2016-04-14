# coding: utf-8
import datetime
from django.shortcuts import render

from django.db.models import Q
from django.db.models import Count
from apps.accounts.models import User
from apps.blog.models import Category
from apps.blog.models import Subcategory
from apps.blog.models import Topic


def home(request):
	context = {}
	context['title'] = u'Главная'
	context['now'] = datetime.datetime.now()
	context['users'] = User.objects.all()
	return render(request, 'main.html', context)


def search(request):
	context = {}
	context['title'] = u'Поиск'
	topics = Topic.objects.all()
	if 'title' in request.GET and request.GET['title']:
		title = request.GET.get('title', '')
		topics = topics.filter(Q(title__icontains=title))
	context['topics'] = topics

	return render(request, 'search.html', locals())