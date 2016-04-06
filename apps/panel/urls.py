from django.conf.urls import url

from . import views


urlpatterns = [
	url(r'^panel/$', views.panel, name='panel'),
	url(r'^users/$', views.users, name='users'),
	url(r'^languages/$', views.languages, name='languages'),
	url(r'^topics/$', views.topics, name='topics'),
	url(r'^posts/$', views.posts, name='posts'),

	# url(r'^(?P<slug>[\w-]+)/$', views.language, name='language'),
	# url(r'^sale/(?P<id>\d+)/$', views.sale, name='sale'),

]