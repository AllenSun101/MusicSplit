from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.say_hello),
    path('yt_to_mp3/', views.yt_to_mp3),
    path('mp3_to_midi/', views.mp3_to_midi),
    path('join_stems/', views.join_stems),
    path('csrf-token/', views.get_csrf_token),
]