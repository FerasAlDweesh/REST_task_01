from rest_framework import serializers
from .models import Flight, Booking

class FlightListSerializer(serializers.ModelSerializer):
	class Meta:
		model = Flight
		fields = ["id", "destination", "time", "price", ]

class BookingListSerializer(serializers.ModelSerializer):
	class Meta:
		model = Booking
		fields = ["flight", "date", "id",]