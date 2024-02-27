import os

import environ
from celery import Celery
from celery.schedules import crontab
from django.conf import settings


env = environ.Env()
env.read_env(f"{os.getcwd()}/.env")
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

app = Celery('dictionary')
app.config_from_object('django.conf:settings', namespace='CELERY')

# Define the schedule for your daily task
# app.conf.beat_schedule = {
#     'send_to_channel': {
#         'task': 'dictionary.tasks.send_to_channel',
#         'schedule': crontab(minute='*/1'),  # Run every 5 minutes
#     },
# }

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()
