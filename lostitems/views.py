from rest_framework import generics
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .models import LostItem, Answer, Guess
from .serializers import LostItemInputSerializer, LostItemListSerializer, AnswerSerializer, GuessSerializer, LostItemOutputSerializer, LostItemInputSerializer, LostItemListSerializer
from rest_framework.pagination import PageNumberPagination, Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .permissions import IsFounder

class StandardResultsSetPagination(PageNumberPagination):

    page_size = 25
    page_size_query_param = "page_size"
    max_page_size = 1000


class LostItemCreateView(generics.CreateAPIView):
    queryset = LostItem.objects.all()
    serializer_class = LostItemInputSerializer
    permission_classes =[IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(founder=self.request.user)


class LostItemListView(generics.ListAPIView):
    queryset = LostItem.objects.all()
    serializer_class = LostItemListSerializer
    pagination_class = StandardResultsSetPagination


class LostItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = LostItem.objects.all()
    serializer_class = LostItemOutputSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


# class AnswerList(generics.ListCreateAPIView):
#     queryset = Answer.objects.all()
#     serializer_class = AnswerSerializer
#     permission_classes = [IsAuthenticated, IsFounder]
#     lookup_url_kwarg = "item_pk"
#     lookup_field = "item__pk"


#     def get_object(self):
#         queryset = self.get_queryset()
#         obj = get_object_or_404(queryset, **filter)
#         self.check_object_permissions(self.request, obj)
#         return obj

class AnswerList(APIView) :
    permission_classes = [IsAuthenticated, IsFounder]
    def get(self, request, item_pk):
        self.check_object_permissions(request=request, obj=get_object_or_404(LostItem, pk=item_pk))
        queryset = Answer.objects.filter(item__founder=request.user, item__pk=item_pk)
        serializer = AnswerSerializer(queryset,many=True)
        return Response(serializer.data)


class GuessList(generics.ListCreateAPIView):
    queryset = Guess.objects.all()
    serializer_class = GuessSerializer

    lookup_url_kwarg = "item_pk"
    lookup_field = "item__pk"

