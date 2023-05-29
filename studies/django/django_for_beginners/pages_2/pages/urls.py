from django.urls import path
from .views import example_function_view

urlpatterns = [
    path('', example_function_view)
]