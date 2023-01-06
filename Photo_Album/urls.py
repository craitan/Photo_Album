
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Photo_Album.common.urls')),
    path('account/', include('Photo_Album.accounts.urls')),
]
