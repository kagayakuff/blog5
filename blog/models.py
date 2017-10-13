from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    created_time = models.DateTimeField(default=timezone.now)
    modified_time = models.DateTimeField(auto_now=True)
    excerpt = models.CharField(max_length=200, blank=True)
    views = models.PositiveIntegerField(default=0)
    author = models.ForeignKey(User)
    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_time']
