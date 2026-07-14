from django.urls import path

from .views import SignupUserView, LoginUserView

urlpatterns = [
    path("signup/",SignupUserView.as_view() ),
    path("login/", LoginUserView.as_view()),
]