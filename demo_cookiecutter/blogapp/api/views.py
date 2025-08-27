from rest_framework import permissions
from rest_framework import viewsets

from demo_cookiecutter.blogapp.api.serializers import BlogSerializer
from demo_cookiecutter.blogapp.models import Blog


class BlogViewSet(viewsets.ModelViewSet[Blog]):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [permissions.IsAuthenticated]
