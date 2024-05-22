from habits import models, serializers, permissions, paginators
from rest_framework import generics


class HabitListAPIView(generics.ListAPIView):
    queryset = models.Habit.objects.all()
    serializer_class = serializers.HabitSerializer
    pagination_class = paginators.HabitPaginator


class UsersHabitListAPIView(HabitListAPIView):
    permission_classes = [permissions.OwnerListOnly]


class PublicHabitListAPIView(HabitListAPIView):
    permission_classes = [permissions.PublicListOnly]


class HabitCreateAPIView(generics.CreateAPIView):
    serializer_class = serializers.HabitSerializer


class HabitUpdateAPIView(generics.UpdateAPIView):
    serializer_class = serializers.HabitSerializer
    queryset = models.Habit.objects.all()
    permission_classes = [permissions.IsOwner]


class HabitDestroyAPIView(generics.DestroyAPIView):
    queryset = models.Habit.objects.all()
    permission_classes = [permissions.IsOwner]
