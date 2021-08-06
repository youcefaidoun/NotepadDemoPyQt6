from django.db import models
import datetime
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.

class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    slug = models.SlugField(null=True,blank=True)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(blank=True, default=datetime.datetime.now)
    active = models.BooleanField(default=True)
    tags = models.CharField(max_length=100, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Note, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
