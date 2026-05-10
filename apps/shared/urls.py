from django.urls import path
from .views import BannerListView, ContactInfoView, GalleryImageListView, ContactMessageCreateView

urlpatterns = [
    path('banners/', BannerListView.as_view(), name='banner-list'),
    path('contact-info/', ContactInfoView.as_view(), name='contact-info'),
    path('gallery/', GalleryImageListView.as_view(), name='gallery-list'),
    path('contact/', ContactMessageCreateView.as_view(), name='contact-message'),
]
