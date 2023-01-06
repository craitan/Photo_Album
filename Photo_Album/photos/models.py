from django.db import models

from Photo_Album.core.validators import validate_letters


class Category(models.Model):
    MAX_LEN_NAME = 100
    name = models.CharField(
        max_length=MAX_LEN_NAME,
        validators=(
            validate_letters,
        ),
        null=False,
        blank=False,
    )

    def __str__(self):
        return self.name


class Photo(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
    )

    image = models.ImageField(
        null=False,
        blank=False,
    )

    description = models.TextField()
