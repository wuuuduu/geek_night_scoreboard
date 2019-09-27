## a Django powered SCOREBOARD SYSTEM

Copyright 2019 Kornel Kołbuk and others contributors. All Rights Reserved. See LICENSE for details.

# Local development:

```bash
sudo apt install libmysqlclient-dev python3-dev rabbitmq-server
sudo systemctl enable rabbitmq-server
sudo systemctl start rabbitmq-server
```

```mysql
CREATE USER 'scoreboard_django_system'@'localhost' IDENTIFIED BY 'scoreboard_django_system';
CREATE DATABASE scoreboard_django_system_local CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
GRANT ALL PRIVILEGES ON `scoreboard_django_system%` . * TO 'scoreboard_django_system'@'localhost';
```

#### virtualenv && virtualenvwrapper

```bash
sudo apt install python3-pip
sudo pip3 install virtualenv
mkdir ~/.virtualenvs
sudo pip3 install virtualenvwrapper
echo 'export WORKON_HOME=$HOME/.virtualenvs' >> ~/.bashrc
echo 'source /usr/local/bin/virtualenvwrapper.sh' >> ~/.bashrc
```
**Restart your all consoles which will be used to run project**
```bash
mkvirtualenv --python=/usr/bin/python3 scoreboard_django_system
echo 'export DJANGO_SETTINGS_MODULE=scoreboard_django_system.settings.local' >> ~/.virtualenvs/scoreboard_django_system/bin/postactivate
workon scoreboard_django_system
```

```bash
pip3 install -r installation/packages/develop.txt
```

```bash
# go to your project dir
cp .env.development.sample .env.development
./manage.py migrate
./manage.py createsuperuser
./manage.py loaddata fixtures/*.json
./manage.py runserver
```


#### Celery
`celery worker -A scoreboard_django_system --loglevel=INFO`

# TRANSLANTIONS
## create new language
```bash
django-admin makemessages -l lang_code
example for the spanish language:
django-admin makemessages -l es
```

## compile translations
```bash
django-admin compilemessages
```

## regenerate translations
```bash
./manage.py makemessages
```