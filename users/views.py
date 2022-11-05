from django.shortcuts import render
from rest_framework.schemas.coreapi import serializers
from rest_framework.views import APIView, Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from .serializers import UserOutputSerializer

# Create your views here.


class RetrieveUserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = UserOutputSerializer(request.user)
        return Response(user.data)
