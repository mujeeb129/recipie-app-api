from django.urls import path
from .views import *


app_name = 'user'
urlpatterns = [
    path('create/', UserCreateView.as_view(), name='create')
]