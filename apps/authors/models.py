from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from uuid import uuid4
from datetime import datetime

# Create your models here.

class Author(AbstractBaseUser):
    id = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    phone = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "author"
        verbose_name = "author"
        verbose_name_plural = "authors"
    
    def __str__(self):
        return self.email

    def has_module_perms(self, app_label):
        return True

    def has_perm(self, perm, obj=None):
        return True


