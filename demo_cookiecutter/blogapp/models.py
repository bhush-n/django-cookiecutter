from django.db import models

from demo_cookiecutter.users.models import BaseModel
from demo_cookiecutter.users.models import User

# Create your models here.


class Blog(BaseModel):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(
        User,
        related_name="blogs",
        on_delete=models.CASCADE,
        null=True,
        default=None,
    )

    def __str__(self):
        return self.title
