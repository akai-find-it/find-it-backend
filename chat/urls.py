from django.urls import path

from . import views

urlpatterns = [
    path("notification/token/", views.AddTokenNotification.as_view(), name="AddTokenNotification"),
]
