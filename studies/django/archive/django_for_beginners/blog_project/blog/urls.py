#!/usr/bin/env python
from django.urls import path
from .views import BlogListView, AboutPageView

urlpatterns = [
	path('', BlogListView.as_view(), name='home'),
	path('about/', AboutPageView.as_view(), name='about'),
]
