"""
WSGI config for famous project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from django.utils.functional import SimpleLazyObject

from famous.wsgi.health_check import health_check

def get_allowed_host_lazy():
    from django.conf import settings

    return settings.ALLOWED_HOSTS[0]

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'famous.settings')

application = get_wsgi_application()

# Apply WSGI middleware here.
# from helloworld.wsgi import HelloWorldApplication
# application = HelloWorldApplication(application)

# application = health_check(application, "/health/")

# # Warm-up the django application instead of letting it lazy-load
# application(
#     {
#         "REQUEST_METHOD": "GET",
#         "SERVER_NAME": SimpleLazyObject(get_allowed_host_lazy),
#         "REMOTE_ADDR": "127.0.0.1",
#         "SERVER_PORT": 80,
#         "PATH_INFO": "/graphql/",
#         "wsgi.input": b"",
#         "wsgi.multiprocess": True,
#     },
#     lambda x, y: None,
# )