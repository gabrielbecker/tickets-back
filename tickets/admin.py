from django.contrib import admin

# Register your models here.
from tickets.events.models import Events
from tickets.tickets.models import Tickets


admin.site.register(Tickets)
admin.site.register(Events)
