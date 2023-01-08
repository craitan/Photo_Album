from django.urls import path

from Photo_Album.photos.views import PhotoGalleryView, add_photo, PhotoView, PhotoDeleteView, CategoryDeleteView

urlpatterns = (
    path('', PhotoGalleryView.as_view(), name='photo gallery'),
    path('add/', add_photo, name='photo add'),
    path('view/<int:pk>', PhotoView.as_view(), name='photo view'),
    path('delete/<int:pk>', PhotoDeleteView.as_view(), name='photo delete'),
    path('category/<int:pk>', CategoryDeleteView.as_view(), name='category delete'),

)
