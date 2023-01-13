from django.db import models
from django.core import validators

from Photo_Album.core.validators import validate_letters


class ContactUs(models.Model):
    MAX_SUBJECT_LENGTH = 20
    MIN_SUBJECT_LENGTH = 2
    MIN_LEN_MESSAGE = 10
    MIN_LEN_FIRST_NAME = 2
    MAX_LEN_FIRST_NAME = 20
    MIN_LEN_LAST_NAME = 2
    MAX_LEN_LAST_NAME = 20

    date_added = models.DateField(
        auto_now_add=True,
        null=False,
        blank=False,
    )

    first_name = models.CharField(
        max_length=MAX_LEN_FIRST_NAME,
        validators=(
            validators.MinLengthValidator(MIN_LEN_FIRST_NAME),
            validate_letters,
        ),
        null=False,
        blank=False,
    )

    last_name = models.CharField(
        max_length=MAX_LEN_LAST_NAME,
        validators=(
            validators.MinLengthValidator(MIN_LEN_LAST_NAME),
            validate_letters,
        ),
        null=False,
        blank=False,
    )

    subject = models.CharField(
        max_length=MAX_SUBJECT_LENGTH,
        validators=(
            validators.MinLengthValidator(MIN_SUBJECT_LENGTH),
        ),
        null=False,
        blank=False,
    )

    email = models.EmailField(
        null=False,
        blank=False,
    )

    massage = models.TextField(
        max_length=250,
        validators=(
            validators.MinLengthValidator(MIN_LEN_MESSAGE),
        ),
        null=False,
        blank=False,
    )

    massage_checked = models.BooleanField(
        default=False,
        null=False,
        blank=False,
    )


    def __str__(self):
        return self.subject

