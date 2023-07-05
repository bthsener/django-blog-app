from django.urls import path
from post.views import *

urlpatterns = [
    path('index/', post_index, name='index'),
    path('details/<int:id>/', post_details, name='details'),
    path('create/', post_create, name='create'),
    path('update/<int:id>/', post_update, name='update'),
    path('delete/<int:id>/', post_delete, name='delete'),
]
