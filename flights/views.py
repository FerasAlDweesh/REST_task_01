from .models import Flight, Booking
from rest_framework.generics import ListAPIView
from .serializers import FlightListSerializer, BookingListSerializer
from datetime import datetime


todays_date = datetime.now()

class FlightList(ListAPIView):
	queryset = Flight.objects.all()
	serializer_class = FlightListSerializer

class BookingList(ListAPIView):
	queryset = Booking.objects.filter(date__gte=todays_date)
	serializer_class = BookingListSerializer