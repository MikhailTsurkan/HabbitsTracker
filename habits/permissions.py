from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user


class OwnerListOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        view.queryset = view.queryset.filter(user=request.user)
        return True
