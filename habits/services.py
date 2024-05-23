import requests
from django.conf import settings


def send_telegram(message, chat_id):
    params = {
        "chat_id": chat_id,
        "text": message,
    }
    requests.post(
        url=settings.TELEGRAM_BOT_URL,
        json=params
    )


def send_habits_tg_notifications(habits):
    for habit in habits:
        reward_habit = None
        reward = None
        if habit.related_habit:
            reward_habit = (f"Привычка {habit.related_habit.action}, "
                            f"выполнить за {habit.related_habit.perform_in}")
        else:
            reward = habit.reward

        message = (f"Время выполнять привычку!\n"
                   f"Место: {habit.place}\n"
                   f"Действие: {habit.action}\n"
                   f"Награда: {reward_habit or reward}")
        send_telegram(message, habit.user.telegram_chat_id)
