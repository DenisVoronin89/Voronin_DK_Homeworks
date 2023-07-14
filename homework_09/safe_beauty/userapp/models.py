from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class MyUser(AbstractUser):
    email = models.EmailField(unique=True)


class ViewHistory(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    viewed_item = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']
