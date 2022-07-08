from django.urls import path
from .views import *


urlpatterns = [
    path('', FeedView.as_view({'get': 'list_feed'})),
    path('<int:pk>', FeedView.as_view({'get': 'retrieve_feed'})),
]
