from django.shortcuts import render
from django.views import generic
from .models import *


def index(request):
    data = {
        'movies_count': Movie.objects.all().count(),
        'actors_count': Actor.objects.all().count(),
        'free_count': Movie.objects.filter(subscription__movie=1)
    }
    return render(request, 'index.html', context=data)


class MoviesList(generic.ListView):
    model = Movie
