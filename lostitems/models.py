from django.db import models
from categories.models import Category, Question
from django.conf import settings

def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)

class LostItem(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField()
    found_at = models.DateField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    founder = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    #image_url = models.ImageField(upload_to=upload_to, blank=True, null=True)
    image_url = models.ImageField(upload_to=upload_to, blank=True, null=True)

    class Meta:
        ordering = ["-created_at", "title"]

    def __str__(self):
        return f"Lost item: {self.title}"


class Answer(models.Model):
    item = models.ForeignKey(LostItem, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    value = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_at", "question"]

    def __str__(self):
        return f"Answer for lost item {self.item}"


class Guess(models.Model):
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    value = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_at", "user"]

    def __str__(self):
        return f"Proposed answer for answer {self.answer}"
