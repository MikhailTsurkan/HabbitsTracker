from rest_framework import serializers
from django.contrib.auth import get_user_model
from users import validators


User = get_user_model()


class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["email", "password", "password2", "telegram_chat_id"]
        validators = [validators.MatchingPasswordsValidator()]

    def save(self, *args, commit=True,  **kwargs):
        self.instance = User(
            email=self.validated_data.get("email"),
            telegram_chat_id=self.validated_data.get("telegram_chat_id"),
        )

        self.instance.set_password(self.validated_data.get("password"))
        if commit:
            self.instance.save()
        return self.instance
