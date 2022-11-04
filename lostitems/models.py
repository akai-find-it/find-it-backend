from django.db import models
from categories.models import Category, Question
from django.conf import settings


class LostItem(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    found_at = models.DateField()
    category = models.ForeignKey(Category)
    founder = models.ForeignKey(settings.AUTH_USER_MODEL)
    created_at = models.DateTimeField(auto_now_add=True)


class Answer(models.Model):
    item = models.ForeignKey(LostItem)
    question = models.ForeignKey(Question)
    value = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Guess(models.Model):
    answer = models.ForeignKey(Answer)
    value = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    created_at = models.DateTimeField(auto_now_add=True)