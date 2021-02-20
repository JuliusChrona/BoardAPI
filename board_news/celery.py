from __future__ import absolute_import

import os

import django
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "board_news.settings")
django.setup()

app = Celery("board_news")

app.config_from_object("django.conf:settings")
app.autodiscover_tasks()

app.conf.beat_schedule = {
    "update_every_midnight": {
        "task": "board_api.tasks.reset_upvotes",
        "schedule": crontab(minute=0, hour=0),
    }
}
