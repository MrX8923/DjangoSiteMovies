from django.contrib import admin
from django.urls import path
from catalog.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'),
    path('movies/', MoviesList.as_view(), name='all_movies'),
    # path('movie/<int:id>', info, name='info'),
    path('movie/<slug:pk>', MovieDetail.as_view(), name='info')

]
