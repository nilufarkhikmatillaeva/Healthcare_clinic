from django.db import models

class Service(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    icon = models.ImageField(upload_to='services/', blank=True, null=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'services'
        verbose_name = 'Service'
        verbose_name_plural = 'Services'

    def __str__(self):
        return self.name
