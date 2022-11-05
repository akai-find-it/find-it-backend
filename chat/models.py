from django.db import models
from django.conf import settings


class NotificationToken(models.Model):
    token = models.CharField(max_length=200)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
