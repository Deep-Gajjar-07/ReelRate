from django.shortcuts import render, get_object_or_404
from django.db.models import Avg

from .models import Movie

# view for show all movies in home page
def index(request):
    movies = Movie.objects.all()
    return render(request, 'movies/index.html',{
        'movies': movies,
    })

# for showing single movie detail with desc & reviews:
def movie_detail(request, id):
    movie = get_object_or_404(Movie, pk=id)
    reviews = movie.reviews.all()
    avg_rating = reviews.aggregate(Avg('rating'))['rating__avg']
    return render(request, 'movies/movie_detail.html', {
        'movie': movie,
        'reviews': reviews,
        'avg_rating': avg_rating,
    })