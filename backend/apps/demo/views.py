from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from .models import Post
from .serializers import PostSerializer

class PostPagination(PageNumberPagination):
    page_size = 10
    max_page_size = 100
    page_size_query_param = 'page_size'

class PostViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Post.objects.order_by('-timestamp')
    serializer_class = PostSerializer
    pagination_class = PostPagination