from django.urls import path

from Photo_Album.photos.views import PhotoGalleryView, PhotoAddView, PhotoView, PhotoEditView, PhotoDeleteView

urlpatterns = (
    path('', PhotoGalleryView.as_view(), name='photo gallery'),
    path('add/', PhotoAddView.as_view(), name='photo add'),
    path('view/<int:pk>', PhotoView.as_view(), name='photo view'),
    path('edit/<int:pk>', PhotoEditView.as_view(), name='photo edit'),
    path('delete/<int:pk>', PhotoDeleteView.as_view(), name='photo delete'),
)
