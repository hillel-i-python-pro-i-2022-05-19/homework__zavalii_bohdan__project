import os
from django.core.asgi import get_asgi_application

os.environ.setdefault("DEFAULT_SETTINGS_MODULE", 'django_proj.settings')

application = get_asgi_application()
