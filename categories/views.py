from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from .models import Category, Question
from .serializers import CategorySerializer, QuestionSerializer


class CategoryListCreate(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class QuestionListView(generics.ListAPIView):
    queryset = Question.objects.all()
    lookup_field = "category__pk"
    lookup_url_kwarg = "category_pk"
    serializer_class = QuestionSerializer

