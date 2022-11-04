from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=30, unique=True)


class Question(models.Model):
    title = models.CharField(max_length=100, unique=True)
    hint = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    required = models.BooleanField(default=False)
