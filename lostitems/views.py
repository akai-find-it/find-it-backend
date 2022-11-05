from rest_framework import generics
from .models import LostItem, Answer, Guess
from .serializers import LostItemSerializer, AnswerSerializer, GuessSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 25
    page_size_query_param = "page_size"
    max_page_size = 1000


class LostItemList(generics.ListCreateAPIView):
    queryset = LostItem.objects.all()
    serializer_class = LostItemSerializer
    pagination_class = StandardResultsSetPagination
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(founder=self.request.user)

class LostItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = LostItem.objects.all()
    serializer_class = LostItemSerializer


class AnswerList(generics.ListCreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer


class AnswerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer


class GuessList(generics.ListCreateAPIView):
    queryset = Guess.objects.all()
    serializer_class = GuessSerializer


class GuessDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Guess.objects.all()
    serializer_class = GuessSerializer
