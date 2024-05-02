"""
WSGI config for dj_em_planning project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# No changes from Django Rest Framework creation

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dj_em_planning.settings')

application = get_wsgi_application()
