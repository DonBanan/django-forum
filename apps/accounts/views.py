# -*- coding: utf-8 -*-
from django.conf import settings
from decimal import Decimal

from django.views.decorators.csrf import csrf_exempt

from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.shortcuts import render

from .forms import SingUpForm, ProfileForm

from .models import User

from apps.blog.models import Topic, Post, PersonalMessage


@csrf_exempt
def singup(request):
	context = {}
	context['form'] = SingUpForm(request.POST or None, request.FILES or None)
	if request.POST and context['form'].is_valid():
		new_user = context['form'].save()
		context['new_user'] = new_user
		new_user.backend = 'apps.accounts.auth.EmailOrUsernameModelBackend'
		login(request, new_user)
		return redirect('/', username=new_user.username)

	return render(request, 'accounts/singup.html', context)


def profile(request, id):
	context = {}
	context['title'] = u'Профиль %s' % (User.objects.get(id=id))
	context['profile'] = User.objects.get(id=id)
	context['topics'] = Topic.objects.filter(user=context['profile'])
	context['posts'] = Post.objects.filter(user=context['profile'])
	context['messages'] = PersonalMessage.objects.filter(user=context['profile'])
	return render(request, 'accounts/profile.html', context)


def edit_profile(request, id):
	context = {}
	context['title'] = u'Редактирование профиля %s' % (User.objects.get(id=id))
	instance = request.user
	context['form'] = ProfileForm(request.POST or None, request.FILES or None, instance=instance)
	if context['form'].is_valid():
		context['form'].save()
	return render(request, 'accounts/edit-profile.html', context)


def del_profile(request, id):
	User.objects.get(id=id).delete()
	return HttpResponse('ok')