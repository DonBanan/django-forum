"""
WSGI config for apps project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os, sys

dn = os.path.dirname
PROJECT_ROOT = os.path.abspath( dn(__file__) + '/../')
VENV = os.path.abspath( dn(__file__) + '/../venv/lib/python2.7/site-packages/' )
sys.path.insert(0, VENV )
sys.path.insert(1, PROJECT_ROOT)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "apps.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()