from django.urls import path
from users import views as user_views
from django.contrib.auth import views as auth_views
from .views import CustomLogoutView  # Import the CustomLogoutView

urlpatterns = [
    path("register/", user_views.register, name="register"),
    path("change_password/", user_views.change_password, name="change-password"),
    path("login/",auth_views.LoginView.as_view(template_name="users/login.html"),
        name="login",
    ),
    path("profile/", user_views.profile, name="profile"),
    path("update_profile/", user_views.update_profile, name="update_profile"),
    path("logout/", CustomLogoutView.as_view(), name="logout"),
]
