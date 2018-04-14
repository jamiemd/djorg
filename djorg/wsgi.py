"""
WSGI config for djorg project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import sys, os

from django.core.wsgi import get_wsgi_application

sys.path.insert(0, 'djorg/djorg/wsgi.py')  

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djorg.settings")

application = get_wsgi_application()


