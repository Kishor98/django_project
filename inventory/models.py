from django.db import models
from django.contrib.auth.models import User


class Items(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)
    type = models.CharField(max_length=50, choices=[("Frames","frames"),("Other","other")])
    location = models.TextField()