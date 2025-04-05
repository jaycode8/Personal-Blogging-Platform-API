from django.db import models
from uuid import uuid4
from django.utils import timezone
from apps.authors.models import Author 
from django.contrib.postgres.fields import ArrayField


class Article(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    # tags = ArrayField(models.CharField(max_length=200), default=list, blank=True)
    tags = models.JSONField()
    

    class Meta:
        db_table = "article"
        verbose_name = "article"
        verbose_name_plural = "articles"

    def __str__(self):
        return self.title




