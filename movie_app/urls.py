from django.urls import path
from . import views


urlpatterns = [
    path('directors/', views.director_create_api_view),
    path('directors/<int:id>/', views.director_detail_api_view),
    path('movies/', views.movie_create_api_view),
    path('movies/<int:id>/', views.movie_detail_api_view),
    path('movies/reviews/', views.movies_with_reviews_api_view),
    path('reviews/', views.review_create_api_view),
    path('reviews/<int:id>/', views.review_detail_api_view),
]
