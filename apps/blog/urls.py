from django.conf.urls import url

from . import views


urlpatterns = [
	url(r'^(?P<subcategory_slug>[\w-]+)/topic/(?P<id>\d+)/$', views.topic, name='topic'),
	url(r'^add-topic/(?P<slug>[\w-]+)/$', views.add_topic, name='add_topic'),
	url(r'^edit-topic/(?P<id>\d+)/$', views.edit_topic, name='edit_topic'),
	url(r'^delete-topic/(?P<id>\d+)/$', views.del_topic, name='del_topic'),


	url(r'^moderated-topic/(?P<id>\d+)/$', views.moderated, name='moderated'),


	url(r'^add-post/(?P<id>\d+)/$', views.add_post, name='add_post'),
	url(r'^edit-post/(?P<id>\d+)/$', views.edit_post, name='edit_post'),
	url(r'^del-post/(?P<id>\d+)/$', views.del_post, name='del_post'),


	url(r'^good-vote/(?P<id>\d+)/$', views.good_vote, name='good_vote'),
	url(r'^bad-vote/(?P<id>\d+)/$', views.bad_vote, name='bad_vote'),


	url(r'^personal-message/(?P<id>\d+)/$', views.personal_message, name='personal_message'),
	url(r'^send-message/(?P<id>\d+)/$', views.send_message, name='send_message'),
	url(r'^delete-message/(?P<id>\d+)/$', views.del_message, name='del_message'),
	url(r'^del-recipient-message/(?P<id>\d+)/$', views.del_recipient_message, name='del_recipient_message'),


	url(r'^tag/(?P<id>\d+)/$', views.tag, name='tag'),


	url(r'^all-language/$', views.all_language, name='all_language'),
	url(r'^(?P<slug>[\w-]+)/$', views.language, name='language'),
	url(r'^(?P<category_slug>[\w-]+)/(?P<subcategory_slug>[\w-]+)/$', views.subcategory, name='subcategory'),


]