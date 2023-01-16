import os

from celery import Celery

EMAIL_SENDING_TIME = 60
try:
    from auto_emails.models import Configuration
    EMAIL_SENDING_TIME = Configuration.objects.first().message_time_in_sec_threshold
except:
    pass

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'copenotes_gencay.settings')

app = Celery('copenotes_gencay')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()



app.conf.timezone = 'UTC'
#Periodic Tasks
app.conf.beat_schedule = {


'email_scheduler':{
        'task':'auto_emails.tasks.email_sender',
        'schedule': EMAIL_SENDING_TIME,
    },
       
    
}