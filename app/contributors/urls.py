from django.urls import path
from contributors.views import main

urlpatterns = [
    path('', main)
]
