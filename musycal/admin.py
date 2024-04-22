from django.contrib import admin

from musycal.models import Album, Genre, Musician, Song

# Register your models here.
class MusicianAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'instrument']
    search_fields = ['first_name', 'last_name', 'instrument']
    list_filter = ['instrument']
    search_help_text = "Search by first name, last name, instrument"
    #fields = ['first_name', 'last_name', 'instrument']
    #exclude = ['registration_date', 'last_updated']
    # fieldsets = [
    #     ('Personal Information', {'fields': ['first_name', 'last_name', 'instrument']}),
    #     ('Website Specific Information', {
    #         'classes': ['collapse'],
    #         'fields': ['slug']
    #         }),
    # ]

class AlbumAdmin(admin.ModelAdmin):
    list_display = ['artist', 'name', 'release_date']
    search_fields = ['artist__first_name', 'artist__last_name', 'name']
    list_filter = ['release_date']
    search_help_text = "Search by artist first name, last name, album name"
    #fields = ['artist', 'name', 'release_date']
    #exclude = ['registration_date', 'last_updated']
    fieldsets = [
        ('Artist Information', {'fields': ['artist']}),
        ('Album Information', {'fields': ['name', 'release_date']}),
    ]

class SongAdmin(admin.ModelAdmin):
    list_display = ['name', 'track_number', 'album']
    search_fields = ['name', 'album__name']
    list_filter = ['album']
    search_help_text = "Search by song name, album name"
    #fields = ['name', 'track_number', 'album', 'genre']
    #exclude = ['registration_date', 'last_updated']
    fieldsets = [
        ('Song Information', {'fields': ['name', 'track_number', 'album']}),
        ('Genre Information', {'fields': ['genre']}),
    ]
    
admin.site.site_header = 'Musycal Administration'
admin.site.register(Musician, MusicianAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Song, SongAdmin)
admin.site.register(Genre)