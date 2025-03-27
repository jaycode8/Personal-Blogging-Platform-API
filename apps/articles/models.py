from django.db import models
import uuid
from django.utils import timezone
from django.contrib.auth.models import User
from apps.authors.models import Author 


class Article(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    tags = models.JSONField()

    def __str__(self):
        return self.title




