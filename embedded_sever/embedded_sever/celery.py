from __future__ import absolute_import , unicode_literals 
import os
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'embedded_sever.settings')
app = Celery('embedded_sever')

# namespace = 'CELERY' means all celery-related configuration keys 
#should have a `CELERY_` prefix

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


#app.conf.beat_scheduler = 'django_celery_beat.schedulers.DatabaseScheduler'
