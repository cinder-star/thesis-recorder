"""
WSGI config for thesis_recorder project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os
import sys
import site

site.addsitedir("/var/www/thesis-recorder/venv/lib/python3.8/site-packages")
site.addsitedir("/var/www/thesis-recorder/venv/lib64/python3.8/site-packages")

sys.path.insert(0, "/var/www/thesis-recorder")

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "thesis_recorder.settings")

application = get_wsgi_application()
