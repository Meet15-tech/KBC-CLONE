from django.urls import path

from . import views

urlpatterns = [

    path("", views.home, name="home"),

    path("register/", views.register, name="register"),

    path(

        "fastest-finger/",

        views.fastest_finger,

        name="fastest_finger"

    ),
    path("hotseat/", views.hotseat, name="hotseat"),
    path("start-hotseat/", views.start_hotseat_game, name="start_hotseat_game"),
    path("hotseat/", views.hotseat, name="hotseat"),
    path("leaderboard/", views.leaderboard, name="leaderboard"),  

]