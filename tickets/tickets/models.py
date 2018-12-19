import uuid
from django.db import models
from django.utils import timezone

from tickets.events.models import Events


class Tickets(models.Model):
    id = models.UUIDField('OID', db_column='cd_ticket', default=uuid.uuid4, primary_key=True)
    event = models.ForeignKey(Events, db_column='cd_event', null=False, related_name='tickets', on_delete=models.CASCADE)
    type = models.CharField('Type', db_column='nm_type', max_length=20, default='Full')
    timestamp = models.DateTimeField('Time Stamp', db_column='dt_created', null=False, default=timezone.now)

    class Meta:
        db_table = 'tickets'
        verbose_name = 'Ticket'
        verbose_name_plural = 'Tickets'
        unique_together = ['event', 'type']
