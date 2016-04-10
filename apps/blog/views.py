# coding: utf-8
from django.shortcuts import render, redirect
from django.db.models import F
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required

from .models import Category, Subcategory, Topic, Post, Vote, TopicMessage

from .forms import TopicForm, PostForm, PersonalMessageForm, ModeratedForm


def all_language(request):
	context = {}
	context['title'] = u'Все языки'
	context['languages'] = Category.objects.all()
	return render(request, 'blog/languages.html', context)


def language(request, slug):
	context = {}
	context['title'] = Category.objects.get(slug=slug)
	context['language'] = Category.objects.get(slug=slug)
	return render(request, 'blog/language.html', context)


def subcategory(request, language_slug, subcategory_slug):
	context = {}
	context['title'] = Subcategory.objects.get(slug=subcategory_slug)
	context['subcategory'] = Subcategory.objects.get(programming_language__slug=language_slug, slug=subcategory_slug)
	context['topics'] = Topic.objects.filter(subcategory=context['subcategory'], public=True)
	return render(request, 'blog/subcategory.html', context)


def topic(request, subcategory_slug, id):
	context = {}
	context['title'] = u'Все топики'
	topic = Topic.objects.get(subcategory__slug=subcategory_slug, id=id, public=True)
	context['posts'] = Post.objects.filter(topic=topic).order_by('-created_at')
	topic.count_views += 1
	context['good_vote'] = Vote.objects.filter(topic=topic, good_vote=True).count()
	context['bad_vote'] = Vote.objects.filter(topic=topic, bad_vote=True).count()
	context['post_form'] = PostForm()
	context['count_view'] = Topic.objects.filter(id=topic.id).update(count_views=F('count_views') + 1)
	topic.save()
	context['topic'] = topic
	return render(request, 'topic/topic.html', context)


@login_required
def add_topic(request, slug):
	context = {}
	context['title'] = u'Создать топик'
	subcategory = Subcategory.objects.get(slug=slug)
	context['form'] = TopicForm(request.POST or None, request.FILES or None)
	if context['form'].is_valid():
		new_topic = context['form'].save(commit=False)
		new_topic.user = request.user
		new_topic.subcategory = subcategory
		new_topic.save()
		return redirect('subcategory', subcategory.programming_language.slug, subcategory.slug )
	return render(request, 'topic/add-form.html', context)


@login_required
def edit_topic(request, id):
	context = {}
	context['title'] = u'Редактирование топика'
	instance = Topic.objects.get(user=request.user, id=id)
	context['form'] = TopicForm(request.POST or None, request.FILES or None, instance=instance)
	if instance.user == request.user:
		if context['form'].is_valid():
			context['form'].save()
			return redirect('subcategory', instance.subcategory.programming_language.slug, instance.subcategory.slug )
	return render(request, 'topic/add-form.html', context)


@login_required
def del_topic(request, id):
	context = {}
	context['title'] = u'Удаление топика'
	Topic.objects.get(user=request.user, id=id).delete()
	return HttpResponse('ok')


@login_required
def moderated(request, id):
	context = {}
	topic = Topic.objects.get(id=id, public=True)
	form = ModeratedForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		new_mod = form.save(commit=False)
		new_mod.topic = topic
		new_mod.user = request.user
		topic.moderated = True
		topic.public = False
		topic.save()
		new_mod.save()
	context['form'] = form
	return render(request, 'topic/moderated.html', context)


@login_required
def add_post(request, id):
	context = {}
	topic = Topic.objects.get(id=id, public=True)
	context['post_form'] = PostForm(request.POST or None)
	if context['post_form'].is_valid():
		new_post = context['post_form'].save(commit=False)
		new_post.user = request.user
		new_post.topic = topic
		new_post.save()
		return redirect('topic', topic.subcategory.slug, topic.id)
		context['topic'] = topic
	return render(request, 'topic/add-post.html', context)


@login_required
def edit_post(request, id):
	context = {}
	post = Post.objects.get(user=request.user, id=id)
	context['post_form'] = PostForm(request.POST or None, instance=post)
	if context['post_form'].is_valid():
		context['post_form'].save()
		return redirect('topic', post.topic.subcategory.slug, post.topic.id)
	context['post'] = post
	return render(request, 'topic/edit-post.html', context)


@login_required
def del_post(request, id):
	Post.objects.get(user=request.user, id=id).delete()
	return HttpResponse('ok')


@login_required
def good_vote(request, id):
	context = {}
	topic = Topic.objects.get(id=id, public=True)
	user_vote = Vote.objects.filter(user=request.user.id, topic=topic)
	if not user_vote:
		vote = Vote.objects.create(user=request.user, topic=topic)
		vote.good_vote = 0
		vote.good_vote += 1
		vote.save()
		return HttpResponse('ok')
	else:
		return HttpResponse('error')


@login_required
def bad_vote(request, id):
	context = {}
	topic = Topic.objects.get(id=id, public=True)
	user_vote = Vote.objects.filter(user=request.user.id, topic=topic)
	if not user_vote:
		vote = Vote.objects.create(user=request.user, topic=topic)
		vote.bad_vote = 0
		vote.bad_vote += 1
		vote.save()
		return HttpResponse('ok')
	else:
		return HttpResponse('error')


@login_required
def personal_message(request, id):
	context = {}
	context['title'] = u'Личное сообщение'
	context['topic'] = Topic.objects.get(id=id, public=True)
	context['personal_form'] = PersonalMessageForm(request.POST or None, request.FILES or None)
	if context['personal_form'].is_valid():
		personal_message = context['personal_form'].save(commit=False)
		personal_message.user = request.user
		personal_message.recipient = context['topic'].user
		personal_message.theme = context['topic'].title
		personal_message.topic = context['topic']
		personal_message.save()
	return render(request, 'topic/personal_message.html', context)


@login_required
def send_message(request, id):
	context = {}
	context['title'] = u'Личное сообщение'
	instance = TopicMessage.objects.get(id=id)
	context['personal_form'] = PersonalMessageForm(request.POST or None)
	if context['personal_form'].is_valid():
		personal_message = context['personal_form'].save(commit=False)
		personal_message.user = request.user
		personal_message.recipient = instance.user
		personal_message.parent = instance
		personal_message.theme = instance.theme
		personal_message.save()
	return render(request, 'topic/personal_message.html', context)


@login_required
def del_message(request, id):
	message = TopicMessage.objects.get(user=request.user, id=id)
	message.delete = True
	message.save()
	return HttpResponse('ok')


@login_required
def del_recipient_message(request, id):
	message = TopicMessage.objects.get(recipient=request.user, id=id)
	message.delete_recipient = True
	message.save()
	return HttpResponse('ok')