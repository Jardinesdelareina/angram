from django.urls import path
from .views import *


urlpatterns = [
    path('', ListFollowersView.as_view()),
    path('<int:pk>', FollowerView.as_view()),
]
