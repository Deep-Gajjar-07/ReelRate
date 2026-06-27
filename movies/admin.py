from django.contrib import admin

from .models import Genre, Movie, Review

admin.site.register(Genre)

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'genre', 'release_year')
    search_fields = ('title', 'genre')

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('movie', 'user', 'rating', 'created_at')
    search_fields = ('user', 'rating')