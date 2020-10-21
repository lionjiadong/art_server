"""
WSGI config for art project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
if os.environ.get('ENV') == 'dev':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'art.settings_dev')
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'art.settings_pro')

application = get_wsgi_application()
