from django.urls import path

from Photo_Album.accounts.views import index

urlpatterns = (
    path('', index, name='index'),
)
