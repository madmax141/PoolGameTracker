from django.urls import path
from . import views

app_name = 'pooltracker'
urlpatterns = [
    path('', views.index, name='index'),
    path('addplayer/', views.addplayer, name='addplayer'),
    path('leaderboard/', views.leaderboard, name='leaderboard'),
    path('startgame/', views.startgame, name='startgame'),
    path('activegames/', views.activegames, name='activegames'),
    path('endgame/', views.endgame, name='endgame'),
]