from django.db import models
import datetime
from django.contrib.auth.models import User
# Create your models here.

class Node(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    slug = models.SlugField()
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(blank=True, default=datetime.datetime.now)
    active = models.BooleanField(default=True)
    tags = models.CharField(max_length=100, blank=True)
