from django.urls import path
from . import views


urlpatterns = [
    path('directors/', views.DirectorCreateAPIView.as_view()),
    path('directors/<int:id>/', views.DirectorDetailAPIView.as_view()),
    path('movies/', views.MovieCreateAPIView.as_view()),
    path('movies/<int:id>/', views.MovieDetailAPIView.as_view()),
    path('movies/reviews/', views.MovieWithReviewCreateAPIView.as_view()),
    path('reviews/', views.ReviewCreateAPIView.as_view()),
    path('reviews/<int:id>/', views.ReviewDetailAPIView.as_view()),
]
