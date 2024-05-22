from rest_framework import generics
from users import serializers


class RegistrationAPIVIew(generics.CreateAPIView):
    serializer_class = serializers.RegistrationSerializer
