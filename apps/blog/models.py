# coding: utf-8
from django.db.models import Count
from django.db.models import F
from django.db import models

from ..accounts.models import User


class ProgrammingLang(models.Model):
	title = models.CharField(verbose_name=u'Название', max_length=256)
	short_description = models.TextField(verbose_name=u'Описание')
	slug = models.SlugField(verbose_name=u'Ярлык')

	def __unicode__(self):
		return self.title

	@models.permalink
	def get_absolute_url(self):
		return ('language', (), {'slug': self.slug})

	class Meta:
		verbose_name=u'Язык программирования'
		verbose_name_plural=u'Языки программирования'


class Subcategory(models.Model):
	programming_language = models.ForeignKey(ProgrammingLang, verbose_name=u'Язык', related_name='subcategories')
	title = models.CharField(verbose_name=u'Название', max_length=256)
	slug = models.SlugField(verbose_name=u'Ярлык')

	def __unicode__(self):
		return self.title

	def posts_count(self):
		posts = {}
		sub_objects = self.topics_subcategory.all()
		for topic in sub_objects:
			topic_count = topic.posts.all().count()
			posts['topic_count'] = {
				'count': topic_count
			}
		return posts

	# def posts_count(self):
	# 	titles_with_counts = self.topics_subcategory.all().annotate(issue_count=Count('posts'))
	# 	return titles_with_counts

	class Meta:
		verbose_name=u'Подкатегория'
		verbose_name_plural=u'Подкатегории'


class Topic(models.Model):
	user = models.ForeignKey(User, verbose_name=u'Юзер', related_name='topics_user')
	subcategory = models.ForeignKey(Subcategory, verbose_name=u'Подкатегория', related_name='topics_subcategory')
	title = models.CharField(verbose_name=u'Название', max_length=256)
	tags = models.CharField(verbose_name=u'Теги', max_length=256)
	description = models.TextField(verbose_name=u'Описание')
	created_at = models.DateTimeField(verbose_name=u'Дата создания', auto_now_add=True)
	public = models.BooleanField(verbose_name=u'Публикация', default=True)
	moderated = models.BooleanField(verbose_name=u'Жалоба', default=False)
	count_post = models.PositiveIntegerField(verbose_name=u'Постов', blank=True, null=True)
	count_views = models.PositiveIntegerField(verbose_name=u'Просмотров', default=1)

	def __unicode__(self):
		return self.title

	def good_vote(self):
		return self.votes.filter(good_vote=True).count()

	def bad_vote(self):
		return self.votes.filter(bad_vote=True).count()

	def posts_count(self):
		titles_with_counts = self.topics_subcategory.all().annotate(issue_count=Count('posts'))
		return titles_with_counts

	def last_post(self):
		posts = {}
		sub_objects = self.posts.filter(topic=self).order_by('-created_at')[:1]
		for post in sub_objects:
			posts['post'] = {
				'user': post.user,
				'avatar': post.user.avatar,
				'created_at': post.created_at
			}
		return posts

	class Meta:
		verbose_name=u'Топик'
		verbose_name_plural=u'Топики'


class Post(models.Model):
	user = models.ForeignKey(User, verbose_name=u'Юзер', related_name='posts_user')
	topic = models.ForeignKey(Topic, verbose_name=u'Топик', related_name='posts')
	message = models.TextField(verbose_name=u'Пост')
	created_at = models.DateTimeField(verbose_name=u'Дата создания', auto_now_add=True)
	public = models.BooleanField(verbose_name=u'Публикация', default=True)


class Vote(models.Model):
	user = models.ForeignKey(User, verbose_name=u'Юзер', related_name='votes_user')
	topic = models.ForeignKey(Topic, verbose_name=u'Топик', related_name='votes')
	good_vote = models.DecimalField(verbose_name=u'Хороший голос', max_digits=6, decimal_places=0, blank=True, null=True)
	bad_vote = models.DecimalField(verbose_name=u'Плохой голос', max_digits=6, decimal_places=0, blank=True, null=True)
	created_at = models.DateTimeField(verbose_name=u'Дата создания', auto_now_add=True)


class PersonalMessage(models.Model):
	user = models.ForeignKey(User, verbose_name=u'Юзер', related_name='personalmessage_user', on_delete=models.SET_NULL, null=True)
	recipient = models.ForeignKey(User, verbose_name=u'Юзер получатель', related_name='recipient', blank=True, null=True, on_delete=models.CASCADE)
	parent = models.ForeignKey('self', verbose_name=u'Родитель', related_name='childs', blank=True, null=True, on_delete=models.CASCADE)
	topic = models.ForeignKey(Topic, verbose_name=u'Топик', related_name='personalmessage_votes', blank=True, null=True)
	message = models.TextField(verbose_name=u'Сообщение')
	new = models.BooleanField(verbose_name=u'Новое', default=True)
	trash = models.BooleanField(verbose_name=u'Мусорка', default=False)
	created_at = models.DateTimeField(verbose_name=u'Дата создания', auto_now_add=True)