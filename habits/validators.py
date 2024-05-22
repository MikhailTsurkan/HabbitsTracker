from rest_framework.exceptions import ValidationError


class LeftEmptyValidator:
    def __init__(self, fields, max_fields=None):
        self.max_fields = max_fields or 1
        self.fields = fields

    def __call__(self, value):
        non_empty = 0
        for field in self.fields:
            if value.get(field):
                non_empty += 1

        if non_empty > self.max_fields:
            fields_string = ", ".join(self.max_fields)
            raise ValidationError(f"Среди полей {fields_string} может быть заполнено максимум {self.max_fields}."
                                  f"Вы заполнили {non_empty}")


class PleasantHabitEmptyValidator(LeftEmptyValidator):
    def __call__(self, value):
        if value.get("is_pleasant"):
            super().__call__(value)


class MaxTimeValidator:
    def __init__(self, max_time, message=None):
        self.max_time = max_time
        self.message = message or f"Продолжительность не должна превышать {self.max_time.total_seconds()} секунд"

    def __call__(self, value):
        if value > self.max_time:
            raise ValidationError(self.message)


class IsNotPleasantValidator:
    message = "В качестве связанной привычки можно указать только приятную привычку"

    def __call__(self, value):

        if not value.get("is_pleasant"):
            raise ValidationError(self.message)


class PeriodicityBetweenValidator:
    def __init__(self, _min, _max):
        self._min = _min
        self._max = _max

    def __call__(self, value):
        if not self._min <= value <= self._max:
            raise ValidationError(f"Периодичность не может быть меньше {self._min} и больше {self._max} дней")
