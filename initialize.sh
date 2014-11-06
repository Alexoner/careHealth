#!/bin/sh
django-admin2.py startproject careHealth
python2 manage.py migrate
python2 manage.py startapp register
