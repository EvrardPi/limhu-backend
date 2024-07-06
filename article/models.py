from django.db import models
import uuid


class Article(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False)
    content = models.TextField(null=False, blank=False)
