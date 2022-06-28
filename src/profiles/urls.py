from django.urls import path
from .views import *


urlpatterns = [
    path('profile/<int:pk>/', CustomUserView.as_view({'get': 'retrieve', 'put': 'update'})),
    path('<int:pk>', CustomUserPublicView.as_view({'get': 'retrieve'})),
]
