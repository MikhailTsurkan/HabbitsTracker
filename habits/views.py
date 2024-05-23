from rest_framework import generics, permissions as drf_permissions

from habits import models, serializers, permissions, paginators


class HabitListAPIView(generics.ListAPIView):
    """
    Базовый класс списка привычек
    """
    queryset = models.Habit.objects.all()
    serializer_class = serializers.HabitSerializer
    pagination_class = paginators.HabitPaginator


class UsersHabitListAPIView(HabitListAPIView):
    """
    Эндпоинт списка привычек текущего пользователя
    """
    permission_classes = [drf_permissions.IsAuthenticated, permissions.OwnerListOnly]


class PublicHabitListAPIView(HabitListAPIView):
    """
    Эндпоинт списка публичных привычек
    """
    permission_classes = [permissions.PublicListOnly]


class HabitCreateAPIView(generics.CreateAPIView):
    """
    Эндпоинт создания привычки
    """
    serializer_class = serializers.HabitSerializer
    permission_classes = [drf_permissions.IsAuthenticated]


class HabitUpdateAPIView(generics.UpdateAPIView):
    """
    Эндпоинт обновления привычки
    """
    serializer_class = serializers.HabitSerializer
    queryset = models.Habit.objects.all()
    permission_classes = [drf_permissions.IsAuthenticated, permissions.IsOwner]


class HabitDestroyAPIView(generics.DestroyAPIView):
    """
    Эндпоинт удаления привычки
    """
    queryset = models.Habit.objects.all()
    permission_classes = [drf_permissions.IsAuthenticated, permissions.IsOwner]
