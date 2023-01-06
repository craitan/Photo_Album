from django.contrib import admin

from Photo_Album.common.models import ContactUs


@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    pass
