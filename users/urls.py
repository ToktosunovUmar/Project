from django.urls import path
from . import views


urlpatterns = [
    path('registration/', views.AuthAPIView.as_view()),
    path('confirm/', views.ConfirmAPIView.as_view()),
    path('authorization/', views.AuthorizationAPIView.as_view()),
]