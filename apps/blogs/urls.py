from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BlogViewSet, CategoryListView, TagListView, CommentCreateView

router = DefaultRouter()
router.register('', BlogViewSet, basename='blog')

urlpatterns = [
    path('', include(router.urls)),
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('tags/', TagListView.as_view(), name='tag-list'),
    path('<int:blog_id>/comments/', CommentCreateView.as_view(), name='comment-create'),
]