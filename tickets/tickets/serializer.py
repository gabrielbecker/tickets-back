import django_filters
from rest_framework import serializers

from tickets.tickets.models import Tickets


class TicketSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
    timestamp = serializers.DateTimeField(read_only=True)
    type = serializers.CharField(max_length=20, allow_null=False, allow_blank=False)
    event = serializers.CharField(max_length=50, allow_null=False, allow_blank=False, source='event.name')

    class Meta:
        model = Tickets
        fields = ['id', 'timestamp', 'type', 'event']


class TicketFilter(django_filters.FilterSet):

    type = django_filters.CharFilter(lookup_expr='icontains')
    event = django_filters.CharFilter(lookup_expr='icontains', field_name='event__name')

    class Meta:
        model = Tickets
        fields = ['type', 'event']
