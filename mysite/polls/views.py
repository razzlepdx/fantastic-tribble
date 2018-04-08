from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    """ Creates an HTTP response for the index route. """
    return HttpResponse("Hello, world.  You're at the polls index.")
