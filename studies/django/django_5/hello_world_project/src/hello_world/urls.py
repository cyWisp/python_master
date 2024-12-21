from django.urls import path
from .views import (
    HomePageView,
    AboutPageView,
    ContactPageView,
    InventoryPageView
)

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('inventory/', InventoryPageView.as_view(), name='inventory'),
]