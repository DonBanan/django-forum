# coding: utf-8
import datetime
from django.shortcuts import render

from apps.accounts.models import User
from apps.blog.models import Category


def home(request):
	context = {}
	context['title'] = u'Главная'
	context['now'] = datetime.datetime.now()
	context['languages'] = Category.objects.all()
	context['users'] = User.objects.all()
	return render(request, 'main.html', context)