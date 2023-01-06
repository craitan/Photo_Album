from django.urls import path

from Photo_Album.common.views import ContactView
from Photo_Album.photos.views import PhotoGalleryView

urlpatterns = (
    path('', PhotoGalleryView.as_view(), name='home page'),
    path('contact-us/', ContactView.as_view(), name='contact us')
)
