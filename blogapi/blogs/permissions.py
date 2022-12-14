from rest_framework.permissions import BasePermission
from rest_framework import permissions

class IsCustomAuthPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            print(request.method, permissions.SAFE_METHODS)
            return True
        print(obj.author, request.user)
        return obj.author == request.user