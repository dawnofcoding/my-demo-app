"""
WSGI config for icore project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os
import sys

sys.path.insert(0,'/home/ceberusian/_shared/Ceb/my-demo-app/icore')

from django.core.wsgi import get_wsgi_application

os.environ["DJANGO_SETTINGS_MODULE"] = "icore.settings"

application = get_wsgi_application()
