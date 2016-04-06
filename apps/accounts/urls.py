from apps.accounts.forms import EmailAuthenticationForm
from django.conf.urls import url

from django.utils.translation import ugettext_lazy as _

from .views import *
import django.contrib.auth.views


urlpatterns = [
    url(r'^login/$',
        django.contrib.auth.views.login,
        {
        'template_name': 'accounts/login.html',
        'extra_context': {'title': _('Login')},
        'authentication_form': EmailAuthenticationForm
        },
        name='login'
    ),
    url(r'^logout/$', django.contrib.auth.views.logout_then_login, name='logout'),
    url(r'^singup/$', singup, name='singup'),

    url(r'^password_change/$',
        django.contrib.auth.views.password_change,
        {
            'template_name': 'accounts/password_change.html',
            'extra_context': {'title': _('Change password')}
        },
        name='password_change'
    ),
    url(r'^password_change/done/$',
        django.contrib.auth.views.password_change_done,
        {
            'template_name': 'accounts/password_change_done.html',
            'extra_context': {'title': _('Change password')}
        },
        name='password_change_done'
    ),
    url(r'^password_reset/$',
        django.contrib.auth.views.password_reset,
        {'template_name': 'accounts/password_reset.html'},
        name='password_reset'
    ),
    url(r'^password_reset/done/$',
        django.contrib.auth.views.password_reset_done,
        {'template_name': 'accounts/password_reset_done.html'},
        name='password_reset_done'
    ),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        django.contrib.auth.views.password_reset_confirm,
        {'template_name': 'accounts/password_reset_confirm.html'},
        name='password_reset_confirm'
    ),
    url(r'^reset/done/$',
        django.contrib.auth.views.password_reset_complete,
        {'template_name': 'accounts/password_reset_complete.html'},
        name='password_reset_complete'
    ),
    url(r'^profile/(?P<id>\d+)/$', profile, name='profile'),
    url(r'^edit-profile/(?P<id>\d+)/$', edit_profile, name='edit_profile'),
    url(r'^delete-profile/(?P<id>\d+)/$', del_profile, name='del_profile'),
]