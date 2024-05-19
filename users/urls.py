from django.urls import path
from users.apps import UsersConfig
from users import views


app_name = UsersConfig.name


urlpatterns = [
    path("registration/", views.RegistrationAPIVIew.as_view(), name="registration"),
]
