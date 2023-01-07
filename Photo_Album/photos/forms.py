from django import forms

from Photo_Album.core.form_mixins import AddPlaceholdersMixin, RemoveLabelsMixin
from Photo_Album.photos.models import Photo


class AddPhotoForm(AddPlaceholdersMixin, RemoveLabelsMixin, forms.ModelForm):
    class Meta:
        model = Photo
        exclude = ('user',)

#TODO: WILL REMOVE EDIT
class EditPhotoForm(AddPlaceholdersMixin, RemoveLabelsMixin, forms.ModelForm):
    class Meta:
        model = Photo
        exclude = ('user',)