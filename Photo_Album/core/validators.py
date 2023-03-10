from django.core import exceptions


def validate_letters(value):
    min_letters = 3

    for ch in value:
        if not ch.isalpha() and ch not in [' ']:
            raise exceptions.ValidationError('Only letters are allowed')

    if len(value) < min_letters:
        raise exceptions.ValidationError('Must have at least three letters.')


def username_validator(value):
    min_letters = 3

    for ch in value:
        if not ch.isalnum() and ch not in ['_', '-']:
            raise exceptions.ValidationError('Username must consist only letters, numbers, underscores and dashes.')

    if len(value) < min_letters:
        raise exceptions.ValidationError('Username must have at least three letters.')


def only_numbers_validator(value):
    for ch in value:
        if not ch.isdigit():
            raise exceptions.ValidationError('Only numbers are allowed')