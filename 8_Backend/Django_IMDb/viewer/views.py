from django.shortcuts import render
from django.http import HttpResponse
from django.utils.datastructures import MultiValueDictKeyError
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import Q
from .models import Movie, Director, Actor, Genre
from .constants import COUNTRIES_CHOICES, GENRES, DIRECTORS, MOVIES, ACTORS
from .forms import ContactForm


def hello_world(request, s0):
    add_movies()
    s1 = request.GET.get('s1', '')
    return render(
        request, template_name='hello.html',
        context={'adjectives': [s0, s1, 'beautiful', 'wonderful', "cool", "shit"]}
    )


def get_country_name(country_code):
    for country in COUNTRIES_CHOICES:
        if country[0] == country_code:
            return country[1]


def add_movies():
    for actor in ACTORS:
        if not Actor.objects.filter(name=actor["name"]).filter(date_birth=actor["date_birth"]).exists():
            Actor.objects.create(
                name=actor["name"],
                date_birth=actor["date_birth"],
                country_of_birth=actor["country_of_birth"],
                bio=actor["bio"]
            )

    for director in DIRECTORS:
        if not Director.objects.filter(name=director["name"]).filter(date_birth=director["date_birth"]).exists():
            Director.objects.create(
                name=director["name"],
                date_birth=director["date_birth"],
                country_of_birth=director["country_of_birth"],
                bio=director["bio"]
            )

    for genre in GENRES:
        if not Genre.objects.filter(name=genre["name"]).exists():
            Genre.objects.create(
                name=genre["name"]
            )

    for movie in MOVIES:
        if not Movie.objects.filter(title=movie["title"]).filter(release_year=movie["release_year"]).exists():
            movie_object = Movie.objects.create(
                title=movie["title"],
                release_year=movie["release_year"],
                description=movie["description"],
                average_rating=movie["average_rating"],
                duration=movie["duration"],
                director=Director.objects.filter(name=movie["director"]).first(),
                language=movie["language"],
                trailer_link=movie["trailer_link"],
                genre=Genre.objects.filter(name=movie["genre"]).first(),
                country_of_origin=movie["country_of_origin"],
                # actors=movie.get("actors")
            )
            if movie.get("actors"):
                movie_object.actors.set(Actor.objects.filter(name__in=movie.get("actors")))


def movies(request, movie) -> HttpResponse:
    # instance = Movie.objects.get(id=2)
    # instance.delete()
    print(request)
    movies = Movie.objects.all()

    # check if the database contains movies, if not, create them
    if not movies:
        add_movies()

    print(movies)
    for mov in movies:
        print(mov.title)
        print(mov.release_year)
        print(mov.genre)
        print(mov.average_rating)
        print(mov.duration)
        print(mov.director)

    client_data = request.GET
    print(client_data)
    try:
        return HttpResponse(f"{Movie.objects.get(title=movie).title} Hello {client_data['name']}")

    except MultiValueDictKeyError:
        return HttpResponse(f"{Movie.objects.get(title=movie).title} Hello nameless bastard")

    except KeyError:
        return HttpResponse("Movie not found")

    except Movie.DoesNotExist:
        return HttpResponse("Movie not found")


def about(request):
    movies_data = Movie.objects.all()
    total_movies = movies_data.count()

    context = {
        'total_movies': total_movies
    }

    return render(request, 'about.html', context=context)


class ListMovies(ListView):
    template_name = 'movies.html'
    model = Movie
    context_object_name = 'movies_data'

    def get_queryset(self):
        movies = Movie.objects.all()
        search_query = self.request.GET.get('search')
        if search_query is not None:
            movies = movies.filter(
                Q(title__icontains=search_query) |
                Q(description__icontains=search_query) |
                Q(director__name__icontains=search_query) |
                Q(genre__name__icontains=search_query) |
                Q(actors__name__icontains=search_query) |
                Q(release_year__icontains=search_query) |
                Q(average_rating__icontains=search_query) |
                Q(duration__icontains=search_query) |
                Q(language__icontains=search_query) |
                Q(country_of_origin__icontains=search_query)
            )
            movies = movies.order_by('-release_year', 'title')
        return movies


class ListActors(ListView):
    template_name = 'actors.html'
    model = Actor
    context_object_name = 'actor_data'


class ListDirectors(ListView):
    template_name = 'directors.html'
    model = Director
    context_object_name = 'director_data'


class ListGenres(ListView):
    template_name = 'genres.html'
    model = Genre
    context_object_name = 'genre_data'


class CreateMovie(PermissionRequiredMixin, CreateView):
    template_name = 'create_movie.html'
    model = Movie
    success_url = reverse_lazy('list_movies')
    fields = '__all__'
    permission_required = 'viewer.add_movie'


class CreateActor(PermissionRequiredMixin, CreateView):
    template_name = 'create_actor.html'
    model = Actor
    success_url = reverse_lazy('list_actors')
    fields = '__all__'
    permission_required = 'viewer.add_actor'


class CreateDirector(PermissionRequiredMixin, CreateView):
    template_name = 'create_director.html'
    model = Director
    success_url = reverse_lazy('list_directors')
    fields = '__all__'
    permission_required = 'viewer.add_director'


class DetailMovie(DetailView):
    template_name = 'detail_movie.html'
    model = Movie
    context_object_name = 'movie'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        country_code = context['movie'].country_of_origin
        country_name = get_country_name(country_code)

        context['country_name'] = country_name

        return context


class DetailActor(DetailView):
    template_name = 'detail_actor.html'
    model = Actor
    context_object_name = 'actor'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        country_code = context['actor'].country_of_birth
        country_name = get_country_name(country_code)

        context['country_name'] = country_name

        return context


class DetailDirector(DetailView):
    template_name = 'detail_director.html'
    model = Director
    context_object_name = 'director'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        country_code = context['director'].country_of_birth
        country_name = get_country_name(country_code)

        context['country_name'] = country_name

        return context


class DetailGenre(DetailView):
    template_name = 'detail_genre.html'
    model = Genre
    context_object_name = 'genre'


class UpdateMovie(PermissionRequiredMixin, UpdateView):
    template_name = 'update_movie.html'
    model = Movie
    success_url = reverse_lazy('list_movies')
    fields = '__all__'
    permission_required = 'viewer.change_movie'


class UpdateActor(PermissionRequiredMixin, UpdateView):
    template_name = 'update_actor.html'
    model = Actor
    success_url = reverse_lazy('list_actors')
    fields = '__all__'
    permission_required = 'viewer.change_actor'


class UpdateDirector(PermissionRequiredMixin, UpdateView):
    template_name = 'update_director.html'
    model = Director
    success_url = reverse_lazy('list_directors')
    fields = '__all__'
    permission_required = 'viewer.change_director'


class DeleteMovie(PermissionRequiredMixin, DeleteView):
    template_name = 'delete_movie.html'
    model = Movie
    success_url = reverse_lazy('list_movies')
    context_object_name = 'movie'
    permission_required = 'viewer.delete_movie'


class DeleteActor(PermissionRequiredMixin, DeleteView):
    template_name = 'delete_actor.html'
    model = Actor
    success_url = reverse_lazy('list_actors')
    context_object_name = 'actor'
    permission_required = 'viewer.delete_actor'


class DeleteDirector(PermissionRequiredMixin, DeleteView):
    template_name = 'delete_director.html'
    model = Director
    success_url = reverse_lazy('list_directors')
    context_object_name = 'director'
    permission_required = 'viewer.delete_director'


class ContactPage(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('list_movies')

    def form_valid(self, form):
        print("Form received!")
        print(form.cleaned_data)
        return super().form_valid(form)

# def movie_thor(request) -> HttpResponse:
#     return HttpResponse(movie_database["Thor"])


# def movie_top_gun(request) -> HttpResponse:
#     return HttpResponse(movie_database["Top Gun"])
