from django.urls import path
from .views import *


urlpatterns = [
    path('<int:pk>', PostListView.as_view()),

    path('post', PostView.as_view({'post': 'create'})),
    path('post/<int:pk>', PostView.as_view({
        'get': 'retrieve_post', 
        'put': 'updat_post', 
        'delete': 'destroy_post'
    })),

    path('comment', CommentView.as_view({'post': 'create'})),
    path('comment/<int:pk>', CommentView.as_view({
        'put': 'update_comment', 
        'delete': 'destroy_comment'
    })),
]
