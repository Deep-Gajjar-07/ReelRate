from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Avg
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .models import Movie, Review, Genre

# view for show all movies in home page
def index(request):
    movies = Movie.objects.all().order_by('-id')
    return render(request, 'movies/index.html',{
        'movies': movies,
    })

# for showing single movie detail with desc & reviews:
def movie_detail(request, id):
    movie = get_object_or_404(Movie, pk=id)
    reviews = movie.reviews.all().order_by('-id')
    avg_rating = reviews.aggregate(Avg('rating'))['rating__avg']
    return render(request, 'movies/movie_detail.html', {
        'movie': movie,
        'reviews': reviews,
        'avg_rating': avg_rating,
    })

#view for browse movies from website:
def browse_movies(request):
    query = request.GET.get('query', '')
    genre_id = request.GET.get('genre', 0)
    movies = Movie.objects.all().order_by('-id')
    genres = Genre.objects.all()

    if genre_id:
        movies = movies.filter(genre_id=genre_id)

    if query:
        movies = movies.filter(title__icontains=query)

    return render(request, 'movies/browse_movies.html', {
        'movies': movies,
        'genres': genres,
        'query': query,
        'genre_id': int(genre_id),
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

# user logout:
def logout_view(request):
    logout(request)
    return redirect('home_page')

# showing user profile details:
@login_required
def user_profile(request):
    total_reviews = request.user.reviews.count()
    user_reviews = request.user.reviews.all()
    user_avg_rating = user_reviews.aggregate(Avg('rating'))['rating__avg']
    return render(request, 'auth/profile.html', {
        'total_reviews': total_reviews,
        'user_avg_rating': user_avg_rating,
    })

# view for auth user can write review
@login_required
def movie_review(request, id):
    movie = get_object_or_404(Movie, id=id)

    if request.method == 'POST':
        rating = request.POST['rating']
        review = request.POST['review']

        if Review.objects.filter(movie=movie, user=request.user).exists():
            return redirect("movie_detail", id=id)
        else:
            Review.objects.create(movie=movie, user=request.user, rating=rating, review=review)
            return redirect("movie_detail", id=id)
        
    return redirect("movie_detail", id=id)

# user can see all there reviews in list:
@login_required
def user_reviews_list(request):
    reviews = Review.objects.filter(user=request.user)

    return render(request, 'movies/user_review_list.html', {
        'reviews': reviews,
    })

# auth user can edit there reviews:
@login_required
def edit_review(request, pk):
    review = get_object_or_404(Review, pk=pk, user=request.user)

    if request.method == 'POST':
        review.rating = request.POST['rating']
        review.review = request.POST['review']
        review.save()

        return redirect('user_review_page')
    return render(request, 'movies/edit_review.html', {
        'review': review
    })

# delete users review:
@login_required
def delete_review(request, pk):
    review = get_object_or_404(Review, pk=pk, user=request.user)
    if request.method == 'POST':
        review.delete()
        return redirect('user_review_page')
    
    return render(request, 'movies/delete_review.html', {'review': review})