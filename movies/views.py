from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Avg
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

from .models import Movie

# view for show all movies in home page
def index(request):
    movies = Movie.objects.all().order_by('-id')
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

# user login view:
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('home_page')
        else:
            return render(request, 'auth/login.html', {'forms': {'errors': True}})
    
    return render(request, 'auth/login.html')

# user register view:
def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            return render(request, 'auth/register.html', {'error': 'Passwords do not match'})

        if User.objects.filter(username=username).exists():
            return render(request, 'auth/register.html', {'error': 'Username already taken'})

        if User.objects.filter(email=email).exists():
            return render(request, 'auth/register.html', {'error': 'Email already registered'})

        user = User.objects.create_user(username=username, email=email, password=password1)
        login(request, user)
        return redirect('home_page')

    return render(request, 'auth/register.html')    