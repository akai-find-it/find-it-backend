from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from .serializeers import NotificationSerializer
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import status
from .utils import send_notification
from .models import NotificationToken


class AddTokenNotification(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def post(self, request, format=None):
        # print(request.user)
        request.data["user"] = request.user.pk
        print(request.data)
        serializer = NotificationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(request.data)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class ChatView(APIView):
    def post(self, request, user_id):
        msg = request.data["text"]
        token = get_object_or_404(NotificationToken, user__pk=user_id)
        user = get_object_or_404(get_user_model(), pk=request.user.pk)

        res, status = send_notification(token=token.token, msg=msg, user=user)
        return Response(res, status)
