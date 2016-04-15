from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^api/json/categories/list/$', views.categories_api, name='categories_api'),
	url(r'^api/json/subcategories/list/$', views.subcategories_api, name='subcategories_api'),
	url(r'^api/json/topics/list/$', views.topics_api, name='topics_api'),
	url(r'^api/json/topic/(?P<id>\d+)/$', views.topic_api, name='topic_api'),
]