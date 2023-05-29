from django.shortcuts import render
from django.http import HttpResponse
import datetime


# Create your views here.
def example_function_view(request):
    now = datetime.datetime.now()
    title = 'example title'

    return HttpResponse(f'Date: <p>{now}</p>')
