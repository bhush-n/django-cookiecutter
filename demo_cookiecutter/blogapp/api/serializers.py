from rest_framework import serializers

from demo_cookiecutter.blogapp.models import Blog
from demo_cookiecutter.users.api.serializers import UserSerializer


class BlogSerializer(serializers.ModelSerializer):
    author_data = UserSerializer(read_only=True, source="author")

    class Meta:
        model = Blog
        fields = serializers.ALL_FIELDS
