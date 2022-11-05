from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return f"{self.name} category"


class Question(models.Model):
    title = models.CharField(max_length=100, unique=True)
    hint = models.TextField()
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="questions"
    )
    required = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title}"
