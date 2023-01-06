from django import forms

from Photo_Album.common.models import ContactUs
from Photo_Album.core.form_mixins import RemoveLabelsMixin, AddPlaceholdersMixin


class ContactUsForm(RemoveLabelsMixin, AddPlaceholdersMixin, forms.ModelForm):
    class Meta:
        model = ContactUs
        exclude = ('massage_checked',)