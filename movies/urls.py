from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="home_page"),
    path('movie-detail/<int:id>/', views.movie_detail, name="movie_detail"),
]
