from django.db import models
from django.contrib.auth.models import User

# model for add genre types for movies:
class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# model for add movie info by admin.
class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=False)
    release_year = models.IntegerField()
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True)
    poster = models.ImageField(upload_to='posters/', blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

# for write review by user:
class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="reviews")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0, choices=[(i,i) for i in range(1, 6)])
    review = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('movie', 'user') # one review per user per movie
