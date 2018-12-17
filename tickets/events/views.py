# Create your views here.
from rest_framework.viewsets import ModelViewSet

from tickets.events.models import Events
from tickets.events.serializer import EventSerializer, EventFilter


class EventsViewSet(ModelViewSet):

    queryset = Events.objects.all()
    serializer_class = EventSerializer
    filter_class = EventFilter
    ordering_fields = '__all__'

