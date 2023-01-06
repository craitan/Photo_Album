from django.contrib import admin

from Photo_Album.photos.models import Category, Photo


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('description',)
