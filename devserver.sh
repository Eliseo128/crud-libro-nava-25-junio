#!/bin/sh
source .venv/bin/activate
python backend_libreria/manage.py runserver $PORT
