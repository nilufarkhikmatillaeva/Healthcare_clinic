from django.contrib import admin
from .models import Doctor

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'specialty', 'is_active']
    search_fields = ['full_name', 'specialty']
    list_filter = ['is_active']