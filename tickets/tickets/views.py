# Create your views here.
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED
from rest_framework.viewsets import ModelViewSet

from tickets.events.models import Events
from tickets.tickets.models import Tickets
from tickets.tickets.serializer import TicketSerializer, TicketFilter


class TicketsViewSet(ModelViewSet):

    queryset = Tickets.objects.all()
    serializer_class = TicketSerializer
    filter_class = TicketFilter
    ordering_fields = '__all__'

    def create(self, request, *args, **kwargs):

        event_id = self.request.data.get('event')
        type = self.request.data.get('type')

        event = Events.objects.get(id=event_id)

        ticket = Tickets()
        ticket.event = event
        ticket.type = type
        ticket.save()

        return Response(status=HTTP_201_CREATED, data=ticket.id)
