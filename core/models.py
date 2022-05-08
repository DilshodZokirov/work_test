from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)


class CategoryUser(models.Model):
    user_id = models.CharField(max_length=100)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
