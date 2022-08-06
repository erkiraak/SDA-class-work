from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import datetime
from .constants import COUNTRIES_CHOICES


class Actor(models.Model):
    name = models.CharField(max_length=100)
    date_birth = models.DateField()
    country_of_birth = models.CharField(max_length=30, choices=COUNTRIES_CHOICES, default='US')
    bio = models.TextField()

    def __str__(self):
        return self.name


class Director(models.Model):
    name = models.CharField(max_length=100)
    date_birth = models.DateField()
    country_of_birth = models.CharField(max_length=30, choices=COUNTRIES_CHOICES, default='US')
    bio = models.TextField()

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=100)
    release_year = models.IntegerField(validators=[MinValueValidator(1888), MaxValueValidator(datetime.now().year)])
    description = models.TextField()
    average_rating = models.FloatField(null=True, blank=True)
    duration = models.PositiveIntegerField()
    director = models.ForeignKey(Director, on_delete=models.DO_NOTHING, null=True, blank=True)
    language = models.CharField(max_length=30, default='english')
    trailer_link = models.URLField(null=True, blank=True)
    genre = models.ForeignKey(Genre, on_delete=models.DO_NOTHING, null=True, blank=True)
    country_of_origin = models.CharField(max_length=30, choices=COUNTRIES_CHOICES, default='US')
    actors = models.ManyToManyField(Actor, blank=True)

    def __str__(self):
        return self.title
