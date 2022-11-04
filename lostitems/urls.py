from django.urls import path
from . import views

urlpatterns = [
    path("lost-items/", views.LostItemList.as_view(), "lost-items"),
]
