from django.contrib import admin

from .models import Genre, Movie

admin.site.register(Genre)

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'genre', 'release_year')
    search_fields = ('title', 'genre')