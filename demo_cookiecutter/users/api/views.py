from rest_framework import permissions
from rest_framework import viewsets

from demo_cookiecutter.users.models import User

from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = "pk"
    permission_classes = [permissions.IsAuthenticated]
