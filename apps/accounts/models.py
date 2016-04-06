# -*- coding: utf-8 -*-
import datetime
from django.core.cache import cache
from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
	avatar = models.FileField(verbose_name=u'Аватар', upload_to='user/avatar')
	vote = models.PositiveIntegerField(verbose_name=u'Голосов', blank=True, null=True)
	is_moderator = models.BooleanField(verbose_name=u'Модератор', default=False)
	rank = models.CharField(verbose_name=u'Звание', max_length=256, blank=True, null=True)

	def last_seen(self):
		return cache.get('seen_%s' % self.username)

	def online(self):
		if self.last_seen():
			now = datetime.datetime.now()
			if now > self.last_seen() + datetime.timedelta(
						 seconds=settings.USER_ONLINE_TIMEOUT):
				return False
			else:
				return True
		else:
			return False
