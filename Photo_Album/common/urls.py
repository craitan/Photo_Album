from django.urls import path

from Photo_Album.common.views import ContactView, HomePageView

urlpatterns = (
    path('', (HomePageView.as_view()), name='home page'),
    path('contact-us/', ContactView.as_view(), name='contact us')
)
