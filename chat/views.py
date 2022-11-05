from django.shortcuts import render
from rest_framework.views import APIView
from .serializeers import NotificationSerializer
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import status
from .utils import send_notification
from .models import NotificationToken


class AddTokenNotification(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, format=None):
        token=NotificationToken.objects.get(user=request.user)
        send_notification(token)
        return Response({})

    def post(self, request, format=None):
        #print(request.user)
        request.data['user']=request.user.pk
        print(request.data)
        serializer = NotificationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(request.data)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
        

