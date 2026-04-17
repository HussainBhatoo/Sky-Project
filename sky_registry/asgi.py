"""
ASGI config for sky_registry project.

It exposes the ASGI callable as a module-level variable named ``application``.

Maintained by: Maurya Patel
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sky_registry.settings')

application = get_asgi_application()
