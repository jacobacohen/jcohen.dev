import imp
import os
import sys


sys.path.insert(0, os.path.dirname(__file__))

from main import application
#wsgi = imp.load_source('wsgi', 'main.py')

#application = wsgi.passenger_wsgi.py
