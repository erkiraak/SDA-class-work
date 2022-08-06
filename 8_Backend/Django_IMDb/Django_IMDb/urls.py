"""Django_IMDb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from viewer.views import (
    hello_world,
    movies,
    about,
    ListMovies,
    ListActors,
    ListDirectors,
    ListGenres,
    CreateMovie,
    CreateActor,
    CreateDirector,
    DetailMovie,
    DetailActor,
    DetailDirector,
    DetailGenre,
    UpdateMovie,
    UpdateActor,
    UpdateDirector,
    DeleteMovie,
    DeleteActor,
    DeleteDirector,
    ContactPage,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("hello/<s0>", hello_world),
    path('about/', about),
    path('', ListMovies.as_view(), name='list_movies'),
    path('actors/', ListActors.as_view(), name='list_actors'),
    path('directors/', ListDirectors.as_view(), name='list_directors'),
    path('genres/', ListGenres.as_view(), name='list_genres'),
    path('create_movie/', CreateMovie.as_view(), name='create_movie'),
    path('create_actor/', CreateActor.as_view(), name='create_actor'),
    path('create_director/', CreateDirector.as_view(), name='create_director'),
    path('title/<int:pk>', DetailMovie.as_view(), name='title'),
    path('actor/<int:pk>', DetailActor.as_view(), name='actor'),
    path('director/<int:pk>', DetailDirector.as_view(), name='director'),
    path('genre/<int:pk>', DetailGenre.as_view(), name='genre'),
    path('title/<int:pk>/update', UpdateMovie.as_view(), name='title_update'),
    path('actor/<int:pk>/update', UpdateActor.as_view(), name='actor_update'),
    path('director/<int:pk>/update', UpdateDirector.as_view(), name='director_update'),
    path('title/<int:pk>/delete', DeleteMovie.as_view(), name='title_delete'),
    path('actor/<int:pk>/delete', DeleteActor.as_view(), name='actor_delete'),
    path('director/<int:pk>/delete', DeleteDirector.as_view(), name='director_delete'),
    path('contact/', ContactPage.as_view(), name='contact'),
    path('accounts/', include('django.contrib.auth.urls')),
]
