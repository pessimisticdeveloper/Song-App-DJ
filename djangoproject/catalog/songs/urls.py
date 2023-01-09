from django.urls import path
from . import views


##songs

urlpatterns = [
    path('',views.index,name='songs'),
    path('<int:song_id>', views.detail, name='detail'),
    path('search',views.search,name='search'),
]