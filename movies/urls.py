from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="home_page"),
    path('movie-detail/<int:id>/', views.movie_detail, name="movie_detail"),
    path('movie-review/<int:id>/', views.movie_review, name="movie_review"),
    path('login/', views.login_view, name="login_page"),
    path('register/', views.register_view, name="register_page"),
    path('logout/', views.logout_view, name="logout"),
    path('profile/', views.user_profile, name="profile_page"),
    path('my-reviews/', views.user_reviews_list, name="user_review_page"),
    path('edit-reviews/<int:pk>/', views.edit_review, name="edit_review"),
    path('delete-reviews/<int:pk>/', views.delete_review, name="delete_review"),
]
