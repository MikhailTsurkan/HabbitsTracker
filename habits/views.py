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
