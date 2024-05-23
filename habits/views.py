from rest_framework import generics, permissions as drf_permissions

from habits import models, serializers, permissions, paginators


class HabitListAPIView(generics.ListAPIView):
    queryset = models.Habit.objects.all()
    serializer_class = serializers.HabitSerializer
    pagination_class = paginators.HabitPaginator


class UsersHabitListAPIView(HabitListAPIView):
    permission_classes = [drf_permissions.IsAuthenticated, permissions.OwnerListOnly]


class PublicHabitListAPIView(HabitListAPIView):
    permission_classes = [permissions.PublicListOnly]


class HabitCreateAPIView(generics.CreateAPIView):
    serializer_class = serializers.HabitSerializer
    permission_classes = [drf_permissions.IsAuthenticated]


class HabitUpdateAPIView(generics.UpdateAPIView):
    serializer_class = serializers.HabitSerializer
    queryset = models.Habit.objects.all()
    permission_classes = [drf_permissions.IsAuthenticated, permissions.IsOwner]


class HabitDestroyAPIView(generics.DestroyAPIView):
    queryset = models.Habit.objects.all()
    permission_classes = [drf_permissions.IsAuthenticated, permissions.IsOwner]
