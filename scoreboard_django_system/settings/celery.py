from celery import Celery

app = Celery('scoreboard_django_system')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
