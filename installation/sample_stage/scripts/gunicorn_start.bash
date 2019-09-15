#!/bin/bash
# http://michal.karzynski.pl/blog/2013/06/09/django-nginx-gunicorn-virtualenv-supervisor/
NAME="scoreboard_django_system"                                  # Name of the application
DJANGODIR=/home/scoreboard_django_system/scoreboard_django_system             # Django project directory
SOCKFILE=/home/scoreboard_django_system/run/gunicorn.sock  # we will communicte using this unix socket
USER=scoreboard_django_system                                        # the user to run as
GROUP=scoreboard_django_system                                     # the group to run as
NUM_WORKERS=2                                     # how many worker processes should Gunicorn spawn
DJANGO_SETTINGS_MODULE=scoreboard_django_system.settings.stage             # which settings file should Django use
DJANGO_WSGI_MODULE=scoreboard_django_system.wsgi                     # WSGI module name

echo "Starting $NAME as `whoami`"

# Activate the virtual environment
cd $DJANGODIR
source /home/scoreboard_django_system/venv/bin/activate
mkdir /home/scoreboard_django_system/mysql_backup/ -p
mkdir /home/scoreboard_django_system/media/protected/ -p
mkdir /home/scoreboard_django_system/scoreboard_django_system/commons -p
mysqldump -u scoreboard_django_system -pscoreboard_django_system scoreboard_django_system_stage > /home/scoreboard_django_system/mysql_backup/"$(date +%s.dump)"
pip3 install -r /home/scoreboard_django_system/scoreboard_django_system/installation/packages/stage.txt
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH
export LANG=en_US.UTF-8
python3 ~/scoreboard_django_system/manage.py migrate --noinput
python3 ~/scoreboard_django_system/manage.py collectstatic --noinput
# Create the run directory if it doesn't exist
RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR

# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
exec /home/scoreboard_django_system/venv/bin/gunicorn ${DJANGO_WSGI_MODULE}:application \
  --name $NAME \
  --timeout 15 \
  --workers $NUM_WORKERS \
  --user=$USER --group=$GROUP \
  --bind=unix:$SOCKFILE \
  --log-level=debug \
  --log-file=-
