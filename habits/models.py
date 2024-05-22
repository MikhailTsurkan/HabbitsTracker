from datetime import datetime

from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()


NULL = {
    "null": True,
    "blank": True
}


class Habit(models.Model):
    """
    Модель, описывающая привычку
    """
    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Пользователь",
        help_text="создатель привычки",
    )

    place = models.CharField(
        max_length=128,
        verbose_name="Место",
        help_text="место, в котором необходимо выполнять привычку",
    )
    perform_at = models.TimeField(
        verbose_name="Время",
        help_text="время, когда необходимо выполнять привычку",
        **NULL
    )
    action = models.CharField(
        max_length=256,
        verbose_name="Действие",
        help_text="действие, которое представляет собой привычка",
    )
    is_pleasant = models.BooleanField(
        default=False,
        verbose_name="Признак приятной привычки",
        help_text="привычка, которую можно привязать к выполнению полезной привычки",
    )
    related_habit = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        verbose_name="Связанная привычка",
        help_text="привычка, которая связана с другой привычкой, \
важно указывать для полезных привычек, но не для приятных",
        **NULL
    )
    periodicity = models.PositiveSmallIntegerField(
        default=1,
        verbose_name="Периодичность",
        help_text="периодичность выполнения привычки для напоминания в днях",
        **NULL
    )
    reward = models.CharField(
        max_length=256,
        verbose_name="Вознаграждение",
        help_text="ем пользователь должен себя вознаградить после выполнения",
        **NULL
    )
    perform_in = models.DurationField(
        verbose_name="Время на выполнение",
        help_text="время, которое предположительно потратит пользователь на выполнение привычки",
    )
    is_public = models.BooleanField(
        default=False,
        verbose_name="Признак публичности",
        help_text="привычки можно публиковать в общий доступ, чтобы другие \
пользователи могли брать в пример чужие привычки"
    )

    next_perform_at = models.DateTimeField(
        verbose_name="Время следующего выполнения",
        help_text="время, в которое нужно выполнить привычку в следующий раз",
        **NULL
    )

    def set_next_perform_at(self):
        now = timezone.now()
        if self.next_perform_at is None or self.next_perform_at < now:
            if self.perform_at <= now.time():
                day = now.today()
            else:
                day = now.today() + 1

            self.next_perform_at = datetime(year=now.year,
                                            month=now.month,
                                            day=day,
                                            hour=self.perform_at.hour,
                                            minute=self.perform_at.hour
                                            )
