from django.db import models

class Banner(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='banners/')
    button_text = models.CharField(max_length=100, blank=True, null=True)
    button_link = models.CharField(max_length=255, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        db_table = 'banners'
        ordering = ['order']

    def __str__(self):
        return self.title


class ContactInfo(models.Model):
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.TextField()
    working_hours = models.CharField(max_length=255)
    map_link = models.URLField(blank=True, null=True)

    class Meta:
        db_table = 'contact_info'

    def __str__(self):
        return self.phone


class GalleryImage(models.Model):
    image = models.ImageField(upload_to='gallery/')
    caption = models.CharField(max_length=255, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        db_table = 'gallery'
        ordering = ['order']

    def __str__(self):
        return self.caption or f"Image {self.id}"

class ContactMessage(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'contact_messages'
        verbose_name = 'Contact Message'
        verbose_name_plural = 'Contact Messages'

    def __str__(self):
        return f"{self.name} - {self.email}"
