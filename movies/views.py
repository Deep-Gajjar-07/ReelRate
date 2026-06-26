from django.shortcuts import render

from .models import Movie

# view for show all movies in home page
def index(request):
    movies = Movie.objects.all()
    return render(request, 'movies/index.html',{
        'movies': movies,
    })