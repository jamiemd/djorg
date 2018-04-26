from uuid import uuid4
from django.contrib.auth.models import User
from django.db import models

class Wiki(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=200)
    content = models.TextField(blank=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    published = models.BooleanField(default=False, verbose_name="Publish?")
    created= models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

class EditWiki(models.Model):
    page = models.ForeignKey(Wiki, related_name='revisions', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField(blank=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    published = models.BooleanField(default=False, verbose_name="Publish?")
    created= models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


