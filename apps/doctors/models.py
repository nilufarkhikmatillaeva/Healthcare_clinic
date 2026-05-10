from django.db import models


class Doctor(models.Model):
    full_name = models.CharField(max_length=255)
    specialty = models.CharField(max_length=255)
    bio = models.TextField(blank=True, null=True)
    photo = models.ImageField(upload_to='doctors/', blank=True, null=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'doctors'
        verbose_name = 'Doctor'
        verbose_name_plural = 'Doctors'

    def __str__(self):
        return self.full_name