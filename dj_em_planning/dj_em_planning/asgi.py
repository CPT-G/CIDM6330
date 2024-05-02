"""
ASGI config for dj_em_planning project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

# Nearly mirrored from djbarky RF4
import os

from channels.routing import ChannelNameRouter, ProtocolTypeRouter
from django.core.asgi import get_asgi_application

from em_planning_api import consumers

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dj_em_planning.settings')

em_planning_asgi_app = get_asgi_application()

# for channels support
application = ProtocolTypeRouter(
    {
        "http": em_planning_asgi_app,
        "channel": ChannelNameRouter(
            {
                "em-data-add": consumers.SimpleEMDataConsumer.as_asgi(),
            }
        ),
    }
)
