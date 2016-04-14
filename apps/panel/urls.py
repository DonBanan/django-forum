from django.conf.urls import url

from . import views


urlpatterns = [
	url(r'^panel/$', views.panel, name='panel'),

	url(r'^panel/users/$', views.users, name='users'),

	url(r'^panel/categories/$', views.categories, name='categories'),
	url(r'^panel/categories/(?P<slug>[\w-]+)/$', views.category, name='category'),

	url(r'^panel/topics/$', views.topics, name='topics'),

	url(r'^panel/posts/$', views.posts, name='posts'),
]