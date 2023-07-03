from django.urls import path
from post.views import *

urlpatterns = [
    path('index/', post_index),
    path('details/', post_details),
    path('create/', post_create),
    path('update/', post_update),
    path('delete/', post_delete),
]
