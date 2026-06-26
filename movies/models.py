from django.db import models


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