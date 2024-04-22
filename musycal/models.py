from django.db import models

# Create your models here.
class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()

    def __str__(self):
        return self.name
    
class Song(models.Model):
    name = models.CharField(max_length=100)
    track_number = models.IntegerField()
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    genre = models.ManyToManyField(Genre)

    def __str__(self):
        return self.name
