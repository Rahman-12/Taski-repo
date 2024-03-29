from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.home, name="home"),
    path("signup/", views.signup, name="signup"),
    path("login/", views.login, name="login"),
    path("task/", views.create_task, name="task")
]
