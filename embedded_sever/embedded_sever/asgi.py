"""
ASGI config for embedded_sever project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

from channels.http import AsgiHandler 
from channels.routing import ProtocolTypeRouter, ChannelNameRouter, URLRouter

from notifications import consumers
from notifications import routing as notifications_routing


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'embedded_sever.settings')
django.setup()


application = ProtocolTypeRouter({
    'http' : AsgiHandler(),
    'websocket': URLRuter(notification_routing.websocket.urlpattern)

})
