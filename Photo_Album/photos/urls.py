from django.urls import path

from Photo_Album.photos.views import PhotoGalleryView, add_photo, PhotoView,  PhotoDeleteView

urlpatterns = (
    path('', PhotoGalleryView.as_view(), name='photo gallery'),
    path('add/', add_photo, name='photo add'),
    path('view/<int:pk>', PhotoView.as_view(), name='photo view'),
    path('delete/<int:pk>', PhotoDeleteView.as_view(), name='photo delete'),
)
