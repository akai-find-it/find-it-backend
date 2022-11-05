from django.urls import path
from . import views

urlpatterns = [
    path("lost-items/", views.LostItemList.as_view()),
    path("lost-items/<int:pk>", views.LostItemDetail.as_view()),
    path("answers/", views.AnswerList.as_view()),
    path("answers/<int:pk>", views.AnswerDetail.as_view()),
    path("guesses/", views.GuessList.as_view()),
    path("guesses/<int:pk>", views.GuessDetail.as_view()),
]
