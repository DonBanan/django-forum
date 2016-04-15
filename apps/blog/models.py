# coding: utf-8
from django.db.models import Count, Avg
from django.db.models import F
from django.db import models

from ..accounts.models import User


class Category(models.Model):
	title = models.CharField(verbose_name=u'Название', max_length=256)
	short_description = models.TextField(verbose_name=u'Описание')
	slug = models.SlugField(verbose_name=u'Ярлык')

	def __unicode__(self):
		return self.title

	@models.permalink
	def get_absolute_url(self):
		return ('language', (), {'slug': self.slug})

	class Meta:
		verbose_name=u'Категория'
		verbose_name_plural=u'Категории'


class Subcategory(models.Model):
	category = models.ForeignKey(Category, verbose_name=u'Язык', related_name='subcategories')
	title = models.CharField(verbose_name=u'Название', max_length=256)
	slug = models.SlugField(verbose_name=u'Ярлык')

	def __unicode__(self):
		return self.title

	def topic_count(self):
		return self.topics_subcategory.count()

	def topic_posts_count(self):
		posts = {}
		topics = self.topics_subcategory.values('posts').annotate(dcount=Count('posts'))
		return topics.count()

	def topic_last_post(self):
		posts = {}
		topics = self.topics_subcategory.all()
		for topic in topics:
			post = Post.objects.filter(topic=topic).order_by("created_at")
			for post_item in post:
				posts['post_item'] = {
					'user': post_item.user,
					'created_at': post_item.created_at,
				}
		return posts


	class Meta:
		verbose_name=u'Подкатегория'
		verbose_name_plural=u'Подкатегории'


class Tag(models.Model):
	word = models.CharField(max_length=35)
	slug = models.CharField(max_length=250)

	def __unicode__(self):
		return self.word


class Topic(models.Model):
	user = models.ForeignKey(User, verbose_name=u'Юзер', related_name='topics_user')
	subcategory = models.ForeignKey(Subcategory, verbose_name=u'Подкатегория', related_name='topics_subcategory')
	title = models.CharField(verbose_name=u'Название', max_length=256)
	tags = models.ManyToManyField(Tag, verbose_name=u'Тэги', related_name='topic_tags')
	description = models.TextField(verbose_name=u'Описание')
	created_at = models.DateTimeField(verbose_name=u'Дата создания', auto_now_add=True)
	public = models.BooleanField(verbose_name=u'Публикация', default=True)
	moderated = models.BooleanField(verbose_name=u'На проверке модером', default=False)
	count_post = models.PositiveIntegerField(verbose_name=u'Постов', blank=True, null=True)
	count_views = models.PositiveIntegerField(verbose_name=u'Просмотров', default=1)

	def __unicode__(self):
		return self.title

	@models.permalink
	def get_absolute_url(self):
		return ('topic', (), {'slug': self.subcategory.slug, 'id': self.id})

	def good_vote(self):
		return self.votes.filter(good_vote=True).count()

	def bad_vote(self):
		return self.votes.filter(bad_vote=True).count()

	def posts_count(self):
		posts_with_counts = self.topics_subcategory.filter(public=True).annotate(issue_count=Count('posts'))
		return posts_with_counts


	class Meta:
		verbose_name=u'Топик'
		verbose_name_plural=u'Топики'


class Moderated(models.Model):
	topic = models.ForeignKey(Topic, verbose_name=u'Топик', related_name='topic_moderated')
	user = models.ForeignKey(User, verbose_name=u'Юзер', related_name='moderated_user')
	text = models.CharField(verbose_name=u'Проблема', max_length=256)
	created_at = models.DateTimeField(verbose_name=u'Дата создания', auto_now_add=True)
	moderated = models.BooleanField(verbose_name=u'Проверил модератор', default=False)


class Post(models.Model):
	user = models.ForeignKey(User, verbose_name=u'Юзер', related_name='posts_user')
	topic = models.ForeignKey(Topic, verbose_name=u'Топик', related_name='posts')
	message = models.TextField(verbose_name=u'Пост')
	created_at = models.DateTimeField(verbose_name=u'Дата создания', auto_now_add=True)
	public = models.BooleanField(verbose_name=u'Публикация', default=False)

	def __unicode__(self):
		return self.message


class Vote(models.Model):
	user = models.ForeignKey(User, verbose_name=u'Юзер', related_name='votes_user')
	topic = models.ForeignKey(Topic, verbose_name=u'Топик', related_name='votes')
	good_vote = models.DecimalField(verbose_name=u'Хороший голос', max_digits=6, decimal_places=0, blank=True, null=True)
	bad_vote = models.DecimalField(verbose_name=u'Плохой голос', max_digits=6, decimal_places=0, blank=True, null=True)
	created_at = models.DateTimeField(verbose_name=u'Дата создания', auto_now_add=True)


class TopicMessage(models.Model):
	user = models.ForeignKey(User, verbose_name=u'Юзер', related_name='personalmessage_user', on_delete=models.SET_NULL, null=True)
	recipient = models.ForeignKey(User, verbose_name=u'Юзер получатель', related_name='recipient', blank=True, null=True, on_delete=models.SET_NULL)
	parent = models.ForeignKey('self', verbose_name=u'Родитель', related_name='childs', blank=True, null=True, on_delete=models.SET_NULL)
	topic = models.ForeignKey(Topic, verbose_name=u'Топик', related_name='personalmessage_votes', blank=True, null=True)
	theme = models.CharField(verbose_name=u'', max_length=500)
	message = models.TextField(verbose_name=u'Сообщение')
	delete = models.BooleanField(verbose_name=u'Удаление юзер', default=False)
	delete_recipient = models.BooleanField(verbose_name=u'Удаление получатель', default=False)
	created_at = models.DateTimeField(verbose_name=u'Дата создания', auto_now_add=True)

	def __unicode__(self):
		return self.theme

	class Meta:
		verbose_name='Сообщение'
		verbose_name_plural=u'Сообщения'