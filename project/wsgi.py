"""
WSGI config for countrybanned project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

try:
    from mod_wsgi import process_group
except ImportError:
    settings_module = 'project.settings.sites_local'
else:
    settings_module = process_group

os.environ['DJANGO_SETTINGS_MODULE'] = settings_module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', os.environ['DJANGO_SETTINGS_MODULE'])

application = get_wsgi_application()
