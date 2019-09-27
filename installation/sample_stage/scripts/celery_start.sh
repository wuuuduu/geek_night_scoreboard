#!/bin/bash
NAME="scoreboard_django_system"                                  # Name of the application
DJANGODIR=/home/scoreboard_django_system/scoreboard_django_system             # Django project directory
DJANGO_SETTINGS_MODULE=scoreboard_django_system.settings.stage             # which settings file should Django use

echo "Starting $NAME - celery"

# Activate the virtual environment
cd $DJANGODIR
source /home/scoreboard_django_system/venv/bin/activate
mkdir /home/scoreboard_django_system/mysql_backup/ -p
mkdir /home/scoreboard_django_system/media/protected/ -p
mkdir /home/scoreboard_django_system/scoreboard_django_system/commons -p
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH
export LANG=en_US.UTF-8
/home/scoreboard_django_system/venv/bin/celery -A scoreboard_django_system control shutdown
exec /home/scoreboard_django_system/venv/bin/celery worker -A scoreboard_django_system --loglevel=INFO
