from django.urls import path
from .views import simple_api

urlpatterns = [
    path('mensaje/', simple_api),
]
