from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Movie(models.Model):
    title=models.CharField(max_length=70)
    genres=models.CharField(max_length=70)
    year=models.DateField()
    image=models.ImageField(upload_to="movie_image")
    movieduration=models.IntegerField()
    description = models.TextField(max_length=250)
    actors = models.CharField(max_length=70)
    link = models.URLField(max_length=250)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return str(self.pk)

class Review(models.Model):
    name= models.CharField(max_length=100)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    review_text = models.TextField()




class Genre(models.Model):
    name = models.CharField(max_length=70)

    def _str_(self):
        return self.name