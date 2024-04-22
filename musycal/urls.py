from django.urls import path

from musycal import views


urlpatterns = [
    path('musicians', views.musicians, name='musicians'),
    path('musicians/<int:id>', views.musician_details, name='musician_details'),
    path('albums', views.albums, name='albums'),
    path('albums/<int:id>', views.album_details, name='album_details'),
    path('songs', views.songs, name='songs'),
    path('songs/<int:id>', views.song_details, name='song_details'),
]
