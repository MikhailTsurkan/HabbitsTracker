from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    """
    Проверка пользователя на обладание сущностью
    """
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user


class BaseListOnly(permissions.BasePermission):
    """
    Базовый класс фильтрации queryset
    """
    def get_filtered_queryset(self, request, queryset):
        raise NotImplementedError

    def has_permission(self, request, view):
        view.queryset = self.get_filtered_queryset(request, view.queryset)
        return True


class OwnerListOnly(BaseListOnly):
    """
    Класс фильтрации по текущему пользователю
    """
    def get_filtered_queryset(self, request, queryset):
        return queryset.filter(user=request.user)


class PublicListOnly(permissions.BasePermission):
    """
    Класс фильтрации по признаку публичности
    """
    def get_filtered_queryset(self, request, queryset):
        return queryset.filter(is_public=True)
