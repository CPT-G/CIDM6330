"""
ASGI config for final_project project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

# from channels.routing import ChannelNameRouter, ProtocolTypeRouter
from django.core.asgi import get_asgi_application

# from barkyapi import consumers

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'final_project.settings')

application = get_asgi_application()

# for channels support

# application = ProtocolTypeRouter(
#     {
#         "http": barky_asgi_app,
#         "channel": ChannelNameRouter(
#             {
#                 "bookmarks-add": consumers.SimpleBookmarkConsumer.as_asgi(),
#             }
#         ),
#     }
# )
