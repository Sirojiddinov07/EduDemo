import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "conf.settings")  # Change `edu` to your project name

app = Celery("conf")
app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks(['edu.tasks.tasks'],)

