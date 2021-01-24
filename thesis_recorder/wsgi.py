"""
WSGI config for thesis_recorder project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os
import sys
import site

from django.core.wsgi import get_wsgi_application

from dotenv import load_dotenv

site.addsitedir("/var/www/thesis-recorder/venv/lib/python3.9/site-packages")

load_dotenv(verbose=True)

sys.path.append("/var/www/thesis-recorder")
sys.path.append("/var/www/thesis-recorder/venv/lib/python3.9/site-packages")

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "thesis_recorder.settings")

application = get_wsgi_application()
