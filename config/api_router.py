from django.conf import settings
from rest_framework.routers import DefaultRouter
from rest_framework.routers import SimpleRouter

from demo_cookiecutter.blogapp.api.views import BlogViewSet
from demo_cookiecutter.users.api.views import UserViewSet

router = DefaultRouter() if settings.DEBUG else SimpleRouter()

router.register("users", UserViewSet)
router.register("blogs", BlogViewSet)


app_name = "api"
urlpatterns = router.urls
