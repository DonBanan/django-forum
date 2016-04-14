# coding: utf-8
from django.shortcuts import render

from django.contrib.auth.decorators import user_passes_test

from ..accounts.models import User
from ..blog.models import Category, Subcategory, Topic, Post, Moderated

from .forms import AddCategoryForm, AddSubcategoryForm


@user_passes_test(lambda u: u.is_superuser)
def panel(request):
	context = {}
	context['title'] = u'Админ панель'
	return render(request, 'panel/panel.html', context)


@user_passes_test(lambda u: u.is_superuser)
def users(request):
	context = {}
	context['title'] = u'Все юзеры'
	context['users'] = User.objects.all()
	return render(request, 'panel/users.html', context)


@user_passes_test(lambda u: u.is_superuser)
def categories(request):
	context = {}
	context['title'] = u'Все категории'
	context['categories'] = Category.objects.all()
	return render(request, 'panel/categories.html', context)


@user_passes_test(lambda u: u.is_superuser)
def category(request, slug):
	context = {}
	context['title'] = Category.objects.get(slug=slug).title
	context['category'] = Category.objects.get(slug=slug)
	context['subcategories'] = Subcategory.objects.filter(category=context['category'])
	return render(request, 'panel/category.html', context)


@user_passes_test(lambda u: u.is_superuser)
def topics(request):
	context = {}
	context[''] = u'Все топики'
	context['topics'] = Topic.objects.all().order_by('created_at')
	context['moderateds'] = Moderated.objects.filter(moderated=False).order_by('-topic__id')
	return render(request, 'panel/topics.html', context)


@user_passes_test(lambda u: u.is_superuser)
def posts(request):
	context = {}
	context[''] = u'Все посты'
	context['posts'] = Post.objects.all().order_by('created_at')
	return render(request, 'panel/posts.html', context)