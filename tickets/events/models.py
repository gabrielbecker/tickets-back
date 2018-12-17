import uuid
from django.db import models
from django.utils import timezone


class Events(models.Model):
    id = models.UUIDField('OID', db_column='cd_event', default=uuid.uuid4, primary_key=True)
    timestamp = models.DateTimeField('Time Stamp', db_column='dt_created', null=False, default=timezone.now)
    name = models.CharField('Name', db_column='nm_name', null=False, max_length=200)

    class Meta:
        db_table = 'events'
        verbose_name = 'Event'
        verbose_name_plural = 'Events'
