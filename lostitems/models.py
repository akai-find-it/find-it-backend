from django.db import models
from categories.models import Category, Question
from django.conf import settings


class LostItem(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField()
    found_at = models.DateField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    founder = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Lost item: {self.title}"


class Answer(models.Model):
    item = models.ForeignKey(LostItem, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    value = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Answer for lost item {self.item}"


class Guess(models.Model):
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    value = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Proposed answer for answer {self.answer}"
