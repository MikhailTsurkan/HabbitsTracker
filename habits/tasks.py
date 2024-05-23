from datetime import timedelta

from celery import shared_task
from django.db.models import F
from django.utils import timezone

from habits import models
from habits.services import send_habits_tg_notifications


@shared_task
def send_telegram_messages():
    qs = models.Habit.objects.filter(next_perform_at__lt=timezone.now()).prefetch_related("user", "related_habit")

    send_habits_tg_notifications(habits=qs)

    qs.update(next_perform_at=F("next_perform_at") + timedelta(days=1) * F("periodicity"))
