from rest_framework import status
from rest_framework.views import APIView

from apps.shared.models import Banner, ContactInfo, GalleryImage
from apps.shared.response import CustomResponse
from apps.shared.serializers import BannerSerializer, ContactInfoSerializer, GalleryImageSerializer, \
    ContactMessageSerializer


class BannerListView(APIView):
    def get(self, request):
        banners =Banner.objects.all()
        serializer = BannerSerializer(banners, many=True)
        return CustomResponse.success(data=serializer.data)

class ContactInfoView(APIView):
    def get(self, request):
        contact = ContactInfo.objects.all()
        serializer = ContactInfoSerializer(contact, many=True)
        return CustomResponse.success(data=serializer.data)


class GalleryImageListView(APIView):
    def get(self, request):
        image = GalleryImage.objects.filter(is_active=True)
        serializer = GalleryImageSerializer(image, many=True)
        return CustomResponse.success(data=serializer.data)

class ContactMessageCreateView(APIView):
    def post(self, request):
        serializer = ContactMessageSerializer(data=request.data)
        if not serializer.is_valid():
            return CustomResponse.error(
                message="Validation error",
                errors=serializer.errors,
            )
        serializer.save()
        return CustomResponse.success(
            data=serializer.data,
            message="Your message has been sent successfully!",
            status_code=status.HTTP_201_CREATED
        )

from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from django.conf import settings
from django.conf.urls.static import static

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def service(request):
    return render(request, 'service.html')

def team(request):
    return render(request, 'team.html')

def gallery(request):
    return render(request, 'gallery.html')

def blog(request):
    return render(request, 'blog.html')

def blog_details(request):
    return render(request, 'blog-details.html')

def appointment(request):
    return render(request, 'appointment.html')
