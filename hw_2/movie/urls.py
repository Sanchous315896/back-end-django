from django.urls import path
from . import views


urlpatterns = [
    path('movies/', views.movies),
    path('movies/<str:id>/', views.movie_by_id),
    path('articles/', views.articles),
    path('articles/<str:id>/', views.articles_by_id),
]
