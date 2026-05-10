from rest_framework import status
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ReadOnlyModelViewSet
from .models import Blog, Category, Tag
from .serializers import BlogSerializer, CategorySerializer, TagSerializer, CommentSerializer
from ..shared.pagination import CustomPageNumberPagination
from ..shared.response import CustomResponse


class BlogViewSet(ReadOnlyModelViewSet):
    serializer_class = BlogSerializer
    pagination_class = CustomPageNumberPagination
    filter_backends = [SearchFilter]
    search_fields = ['title', 'author']

    def get_queryset(self):
        queryset = Blog.objects.all()
        category = self.request.GET.get('category')
        if category:
            queryset = queryset.filter(category__id=category)
        return queryset

class CategoryListView(APIView):
    def get(self,request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return CustomResponse.success(data=serializer.data)


class TagListView(APIView):
    def get(self, request):
        tags = Tag.objects.all()
        serializer = TagSerializer(tags, many=True)
        return CustomResponse.success(data=serializer.data)



class CommentCreateView(APIView):
    def post(self, request, blog_id):
        blog = Blog.objects.get(id=blog_id)
        serializer = CommentSerializer(data=request.data)
        if not serializer.is_valid():
            return CustomResponse.error(
                message="Validation error",
                errors=serializer.errors,
            )
        serializer.save(blog=blog)
        return CustomResponse.success(
            data=serializer.data,
            message="Comment added successfully",
            status_code=status.HTTP_201_CREATED,
        )