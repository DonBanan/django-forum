from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from . import views


admin.autodiscover()

urlpatterns = patterns('',
	# Home
	url(r'^$', views.home, name='home'),

	# Admin
	url(r'^admin/', include(admin.site.urls)),

	#Search
	url(r'^search/$', views.search, name='search'),

	# Panel
	url(r'^', include('apps.panel.urls')),

	#Accounts
	url(r'^', include('apps.accounts.urls')),

	url(r'^', include('apps.chat.urls')),

	#Blog
	url(r'^', include('apps.blog.urls')),

	# Api
	url(r'^', include('apps.api.urls')),
)

# For serve static, media, templates in develop mode
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static('/templates/', document_root=settings.PROJECT_DIR + '/templates/')