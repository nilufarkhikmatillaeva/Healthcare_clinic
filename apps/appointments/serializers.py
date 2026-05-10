from rest_framework import serializers
from .models import Appointment

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ['id', 'full_name', 'phone', 'email', 'doctor', 'service', 'date', 'message']

    def validate_date(self, value):
        from django.utils import timezone
        if value < timezone.now().date():
            raise serializers.ValidationError("Appointment date cannot be in the past.")
        return value