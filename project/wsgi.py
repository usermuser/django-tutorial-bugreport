#/var/www/workspace/django-tutorial-#bugreport
## -*- coding: utf-8 -*-

import os, sys

sys.path.insert(0, '/var/www/workspace/django-tutorial-bugreport/')

sys.path.insert(0, '/var/www/workspace/django-tutorial-bugreport/project')

sys.path.insert(0, '/usr/local/bin/')

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

from django.core.handlers.wsgi import WSGIHandler      
application = WSGIHandler()
