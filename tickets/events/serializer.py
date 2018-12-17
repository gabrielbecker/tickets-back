import django_filters
from rest_framework import serializers

from tickets.events.models import Events


class EventSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
    timestamp = serializers.DateTimeField(read_only=True)
    name = serializers.CharField(max_length=200, allow_null=False, allow_blank=False)

    class Meta:
        model = Events
        fields = ['id', 'timestamp', 'name']


class EventFilter(django_filters.FilterSet):

    name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Events
        fields = ['name']
