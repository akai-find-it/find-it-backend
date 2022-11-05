from django.urls import path

from . import views

urlpatterns = [
    path("categories/", views.CategoryListCreate.as_view(), name="CategoryList"),
    path(
        "categories/<int:id>/questions",
        views.QuestionListView.as_view(),
        name="CategoryList",
    ),
]

