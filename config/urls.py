from django.contrib import admin
from django.urls import path

from reviews.views import reviews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', reviews, name='reviews')
]
