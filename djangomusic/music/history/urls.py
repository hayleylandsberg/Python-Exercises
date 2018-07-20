from django.urls import path

from . import views

urlpatterns = [
    path('', views.artist, name='artist'),
    path("<int:artist_id>/", views.detail, name="detail"),
    path("artist/new", views.new_artist, name="new_artist")
]
