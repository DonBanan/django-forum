# coding: utf-8
import json
import datetime
from django.shortcuts import render

from django.http import HttpResponse

from ..blog.models import Category, Subcategory, Topic, Post


def languages_api(request):
	context = {}
	languages = []
	for language in Category.objects.all():
		language_dict = {
			"id": language.id,
			"title": u'%s' % language.title,
			"short_description": u'%s' % language.short_description,
			"slug": language.slug,
		}
		languages.append(language_dict)
	context['languages'] = languages
	return HttpResponse(json.dumps(context, ensure_ascii=False, indent=4), content_type="application/json; charset=utf-8")


def subcategories_api(request):
	context = {}
	subcategories = []
	for subcategory in Subcategory.objects.all():
		subcategory_dict = {
			"id": subcategory.id,
			"programming_language_id": u'%s' %  subcategory.programming_language.id,
			"programming_language": u'%s' %  subcategory.programming_language,
			"title": u'%s' % subcategory.title,
			"slug": subcategory.slug,
		}
		subcategories.append(subcategory_dict)
	context['subcategories'] = subcategories
	return HttpResponse(json.dumps(context, ensure_ascii=False, indent=4), content_type="application/json; charset=utf-8")


def topics_api(request):
	context = {}
	topics = []
	for topic in Topic.objects.all():
		topic_dict = {
			"id": topic.id,
			"user": u'%s' % topic.user,
			"subcategory": u'%s' % topic.subcategory,
			"title": u'%s' % topic.title,
			"tags": u'%s' % topic.tags,
			"description": u'%s' % topic.description,
			"created_at": u'%s' % topic.created_at,
			"public": u'%s' % topic.public,
			"count_post": u'%s' % topic.count_post,
		}
		topics.append(topic_dict)
	context['topics'] = topics
	return HttpResponse(json.dumps(context, ensure_ascii=False, indent=4), content_type="application/json; charset=utf-8")


def topic_api(request, id):
	context = {}
	topic_item = Topic.objects.get(id=id)
	topic = []
	topic_dict = {
		"id": topic_item.id,
		"user": u'%s' % topic_item.user,
		"subcategory": u'%s' % topic_item.subcategory,
		"title": u'%s' % topic_item.title,
		"tags": u'%s' % topic_item.tags,
		"description": u'%s' % topic_item.description,
		"created_at": u'%s' % topic_item.created_at,
		"public": u'%s' % topic_item.public,
		"count_post": u'%s' % topic_item.count_post,
	}
	topic.append(topic_dict)
	context['topic'] = topic
	return HttpResponse(json.dumps(context, ensure_ascii=False, indent=4), content_type="application/json; charset=utf-8")