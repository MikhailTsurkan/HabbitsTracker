from habits import models, serializers
from rest_framework import generics


class HabitListAPIView(generics.ListAPIView):
    queryset = models.Habit.objects.all()
    serializer_class = serializers
