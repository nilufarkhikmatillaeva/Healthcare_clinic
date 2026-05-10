from django.db import models
from apps.doctors.models import Doctor
from apps.services.models import Service

class Appointment(models.Model):
    class Status(models.TextChoices):
        PENDING = 'pending', 'Pending'
        CONFIRMED = 'confirmed', 'Confirmed'
        CANCELLED = 'cancelled', 'Cancelled'

    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True, related_name='appointments')
    service = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True, related_name='appointments')
    date = models.DateField()
    message = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.PENDING)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'appointments'
        verbose_name = 'Appointment'
        verbose_name_plural = 'Appointments'

    def __str__(self):
        return f"{self.full_name} - {self.date}"