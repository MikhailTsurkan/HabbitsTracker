from django.urls import path
from users.apps import UsersConfig
from users import views
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView


app_name = UsersConfig.name


urlpatterns = [
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),

    path("registration/", views.RegistrationAPIVIew.as_view(), name="registration"),

]
