from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from movies.models import Movie


class Review(models.Model):

    movie = models.ForeignKey(
        Movie,
        on_delete=models.PROTECT,
        related_name="reviews",
    )
    stars = models.IntegerField(
        validators=[
            MinValueValidator(0, "Cannot be lower than 0 stars"),
            MaxValueValidator(5, "Cannot be higher than 0 starts"),
        ]
    )
    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.movie)
