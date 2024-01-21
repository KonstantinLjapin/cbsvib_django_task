#!/bin/bash
# need chmod +
#python app/cbsvib/manage.py makemigrations app;
python app/cbsvib/manage.py migrate;
python app/cbsvib/manage.py createsuperuser --noinput;
python app/cbsvib/manage.py runserver 0.0.0.0:8000
