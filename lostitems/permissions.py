from rest_framework import permissions

class IsFounder(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.founder == request.user
