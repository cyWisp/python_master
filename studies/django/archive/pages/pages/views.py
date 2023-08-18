from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class HomePageView(TemplateView):
    page_title = 'Pages: Home'
    template_name = 'home.html'

class AboutPageView(TemplateView):
    page_title = 'Pages: About'
    template_name = 'about.html'