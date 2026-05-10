"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from apps.shared.views import index, about, contact, service, team, gallery, blog, blog_details, appointment

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('service/', service, name='service'),
    path('team/', team, name='team'),
    path('gallery/', gallery, name='gallery'),
    path('blog/', blog, name='blog'),
    path('blog-details/', blog_details, name='blog-details'),
    path('appointment/', appointment, name='appointment'),
    path('api/v1/doctors/', include('apps.doctors.urls')),
    path('api/v1/services/', include('apps.services.urls')),
    path('api/v1/appointments/', include('apps.appointments.urls')),
    path('api/v1/blogs/', include('apps.blogs.urls')),
    path('api/v1/', include('apps.shared.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


