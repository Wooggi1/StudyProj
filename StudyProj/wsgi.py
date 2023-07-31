"""
WSGI config for StudyProj project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os, sys

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'StudyProj.settings')
sys.path.append('D:\python\django\Lib\site-packages')
sys.path.append('D:\python\projects\StudyProj')
application = get_wsgi_application()
