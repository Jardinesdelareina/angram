from django.urls import path
from .views import *


urlpatterns = [
    path('<int:pk>', PostListView.as_view()),
    path('post', PostView.as_view({'post': 'create'})),
    path('post/<int:pk>', PostView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('comment', CommentsView.as_view({'post': 'create'})),
    path('comment/<int:pk>', CommentsView.as_view({'put': 'update', 'delete': 'destroy'})),
]