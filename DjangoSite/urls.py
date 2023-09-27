from django.contrib import admin
from django.urls import path
from catalog.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'),
    path('movies/', MoviesList.as_view, name='all_movies')
]
