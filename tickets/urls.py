from rest_framework import routers

from tickets.events.views import EventsViewSet
from tickets.tickets.views import TicketsViewSet

router = routers.DefaultRouter()

router.register(r'events', EventsViewSet)
router.register(r'tickets', TicketsViewSet)

urlpatterns = router.urls
