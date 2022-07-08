from django.urls import path
from .views import *


urlpatterns = [
    path('<int:pk>/', CustomUserPublicView.as_view({'get': 'retrieve'})),
    path('profile/<int:pk>/', CustomUserView.as_view({'get': 'retrieve', 'put': 'update'})),
]
