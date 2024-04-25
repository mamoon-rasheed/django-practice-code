from django.db import models

# Create your models here.
class Artist(models.Model):
    # name (varchar 255)
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    genre = models.CharField(max_length=255)
    lakab = models.CharField(max_length=10, null=False, blank=False, default='Bakshi')
    dob = models.DateField(default='2024-04-25')


# Select * from table
# Create, Delete, Update, Insert
# Create table app_Artist (id int, name varchar(255))