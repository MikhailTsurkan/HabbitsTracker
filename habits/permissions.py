from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user


class BaseListOnly(permissions.BasePermission):
    def get_filtered_queryset(self, request, queryset):
        raise NotImplementedError

    def has_permission(self, request, view):
        view.queryset = self.get_filtered_queryset(request, view.queryset)
        return True


class OwnerListOnly(BaseListOnly):
    def get_filtered_queryset(self, request, queryset):
        return queryset.filter(user=request.user)


class PublicListOnly(permissions.BasePermission):
    def get_filtered_queryset(self, request, queryset):
        return queryset.filter(is_public=True)
