from rest_framework import generics
from .models import LostItem, Answer, Guess
from .serializers import LostItemSerializer, AnswerSerializer, GuessSerializer


class LostItemList(generics.ListCreateAPIView):
    queryset = LostItem.objects.all()
    serializer_class = LostItemSerializer


class AnswerList(generics.ListCreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer


class GuessList(generics.ListCreateAPIView):
    queryset = Guess.objects.all()
    serializer_class = GuessSerializer
