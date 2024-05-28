from django.db import models
from django.core.validators import MinValueValidator


class Actor(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Genre(models.Model):
    name = models.CharField(
        max_length=255,
        unique=True
    )

    def __str__(self) -> str:
        return self.name


class CinemaHall(models.Model):
    name = models.CharField(max_length=255)
    rows = models.PositiveIntegerField(
        default=10,
        validators=[
            MinValueValidator(1),
        ]
    )
    seats_in_row = models.PositiveIntegerField(
        default=10,
        validators=[
            MinValueValidator(1),
        ]
    )


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    actors = models.ManyToManyField(
        to=Actor,
        related_name="movies"
    )
    genres = models.ManyToManyField(
        to=Genre,
        related_name="movies"
    )
    duration = models.IntegerField()

    def __str__(self) -> str:
        return self.title
