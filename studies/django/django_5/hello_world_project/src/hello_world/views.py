from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.

class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['header_text'] = 'This is the header'
        context['paragraph_text'] = 'This is a paragraph'

        return context


class AboutPageView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['name'] = 'Rob'
        context['location'] = 'Miami'

        return context

class ContactPageView(TemplateView):
    template_name = 'contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['location'] = 'Rob'
        context['phone_number'] = '555-555-5555'

        return context

class InventoryPageView(TemplateView):
    template_name = 'inventory.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['inventory'] = [
                {
                    'name': 'baton',
                    'price': 25.00
                },
                {
                    'name': 'orange',
                    'price': .50
                },
                {
                    'name': 'lawn mower',
                    'price': 200.00
                }
            ]

        return context
