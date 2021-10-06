from django.urls import path
from . import views

urlpatterns = [
    path('<str:reqGenre>/', views.list_songs),
    path('?genre=<str:reqGenre>', views.list_songs),

    path('', views.home),

]
