from django.urls import path
from . import views

urlpatterns = [
    path("lost-items/", views.LostItemListView.as_view()),
    path("lost-items/new", views.LostItemCreateView.as_view()),
    path("lost-items/<int:pk>", views.LostItemDetail.as_view()),
    path("lost-items/<int:item_pk>/answers/", views.AnswerList.as_view()),
    path("lost-items/<int:item_pk>/answered/", views.AnsweredQuestionsList.as_view()),
    path("lost-items/<int:item_pk>/answers/new", views.AnswerCreateView.as_view()),
    path("lost-items/<int:item_pk>/guesses/", views.GuessList.as_view()),
]
