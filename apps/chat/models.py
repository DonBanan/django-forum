# coding: utf-8

from django.db import models

from ..accounts.models import User


class Chat(models.Model):
	user = models.ForeignKey(User, verbose_name=u'Юзер', related_name='chat_users')
	content = models.CharField(verbose_name=u'Сообщение', max_length=5000)
	created_at = models.DateTimeField(verbose_name=u'Дата написания', auto_now_add=True)

	def __unicode__(self):
		return u'Сообщение от %s' % (self.user)
