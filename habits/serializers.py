from rest_framework import serializers
from habits import models, validators


class HabitSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    related_habit = serializers.IntegerField(validators=[validators.IsPleasantValidator()])
    periodicity = serializers.TimeField(validators=[validators.PeriodicityBetweenValidator(1, 7)])
    perform_in = serializers.DurationField(validators=[validators.MaxTimeValidator(max_time=120)])

    class Meta:
        model = models.Habit
        fields = '__all__'
        validators = [
            validators.NotPleasantHabitEmptyValidator(
                fields_amount=1,
                fields=[
                    "related_habit",
                    "reward",
                ]
            ),
            validators.NotPleasantHabitEmptyValidator(
                fields_amount=3,
                fields=[
                    "perform_at",
                    "periodicity",
                    "next_perform_at",
                ]
            ),
            validators.PleasantHabitEmptyValidator(
                fields_amount=0,
                fields=[
                    "related_habit",
                    "reward",
                    "perform_at",
                    "periodicity",
                    "next_perform_at",
                ]
            )
        ]
