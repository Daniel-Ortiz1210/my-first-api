from turtle import title
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Video(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=60)
    slug = models.SlugField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=1)

    def __str__(self) -> str:
        return f'{self.title}'