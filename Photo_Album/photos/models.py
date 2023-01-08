from django.contrib.auth import get_user_model
from django.db import models

from Photo_Album.core.validators import validate_letters

UserModel = get_user_model()


class Category(models.Model):
    MAX_LEN_NAME = 100

    user = models.ForeignKey(
        UserModel,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
    )

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
    MAX_LEN_DESCRIPTION = 100
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        null=True,
        blank=False,
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    image = models.ImageField(
        null=False,
        blank=False,
    )

    description = models.TextField(
        max_length=MAX_LEN_DESCRIPTION,
    )
