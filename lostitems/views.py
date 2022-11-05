from rest_framework import generics
from rest_framework.views import APIView, status
from django.shortcuts import get_object_or_404
from pprint import pprint
from .models import LostItem, Answer, Guess
from .serializers import (
    LostItemInputSerializer,
    LostItemListSerializer,
    AnswerSerializer,
    GuessSerializer,
    LostItemOutputSerializer,
    LostItemInputSerializer,
    LostItemListSerializer,
)
from rest_framework.pagination import PageNumberPagination, Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .permissions import IsFounder


class StandardResultsSetPagination(PageNumberPagination):

    page_size = 25
    page_size_query_param = "page_size"
    max_page_size = 1000


class LostItemCreateView(APIView):
    def post(self, request):
        request.data["founder"] = request.user.pk
        serializer = LostItemInputSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            item = serializer.save()
            return Response({"id": item.id, **serializer.data}, status.HTTP_201_CREATED)

        return Response(serializer.error_messages, status.HTTP_400_BAD_REQUEST)


class LostItemListView(generics.ListAPIView):
    queryset = LostItem.objects.all()
    serializer_class = LostItemListSerializer
    pagination_class = StandardResultsSetPagination


class LostItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = LostItem.objects.all()
    serializer_class = LostItemOutputSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class AnswerCreateView(APIView):
    def post(self, request):
        serializer = AnswerSerializer(request.data)
        if serializer.is_valid():
            answer = serializer.save()
            return Response(
                {"id": answer.id, **serializer.data}, status.HTTP_201_CREATED
            )
        return Response(serializer.error_messages, status.HTTP_400_BAD_REQUEST)


class AnswerList(APIView):
    permission_classes = [IsAuthenticated, IsFounder]

    def get(self, request, item_pk):
        self.check_object_permissions(
            request=request, obj=get_object_or_404(LostItem, pk=item_pk)
        )
        queryset = Answer.objects.filter(item__founder=request.user, item__pk=item_pk)
        serializer = AnswerSerializer(queryset, many=True)
        return Response(serializer.data)


class GuessList(generics.ListCreateAPIView):
    queryset = Guess.objects.all()
    serializer_class = GuessSerializer

    lookup_url_kwarg = "item_pk"
    lookup_field = "item__pk"
