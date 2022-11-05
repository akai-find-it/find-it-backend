from django.urls import path

from . import views

urlpatterns = [
    path("categories/", views.CategoryListCreate.as_view(), name="CategoryList"),
]

