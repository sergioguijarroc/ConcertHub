from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    UpdateView,
    DeleteView,
)
from .models import Concierto, Artista

# Create your views here.


def index(request):
    return render(request, "concerts_app/panelControl.html")


# region Conciertos


# Usuarios normales
class ConciertoListView(ListView):
    model = Concierto
    template_name = "concerts_app/conciertos/concierto_list.html"


class ConciertoDetailView(DetailView):
    model = Concierto
    template_name = "concerts_app/conciertos/concierto_create.html"


# Staff
class ConciertoCreateView(CreateView):
    model = Concierto
    fields = "__all__"
    success_url = reverse_lazy("concierto_list")
    template_name = "concerts_app/conciertos/concierto_create.html"


class ConciertoDeleteView(DeleteView):
    model = Concierto
    success_url = reverse_lazy("concierto_list")
    template_name = "concerts_app/conciertos/concierto_confirm_delete.html"


class ConciertoUpdateView(UpdateView):
    model = Concierto
    fields = "__all__"
    success_url = reverse_lazy("concierto_list")
    template_name = "concerts_app/conciertos/concierto_update.html"


# endregion
# region Artistas


# Usuarios normales
class ArtistaListView(ListView):
    model = Artista


class ArtistaDetailView(DetailView):
    model = Artista


# Staff
class ArtistaCreateView(CreateView):
    model = Artista
    fields = "__all__"
    success_url = reverse_lazy("concierto_list")
    template_name = "concerts_app/artista_create.html"


class ArtistaDeleteView(DeleteView):
    model = Artista
    success_url = reverse_lazy("artista_list")


class ArtistaUpdateView(UpdateView):
    model = Artista
    fields = "__all__"
    success_url = reverse_lazy("concierto_list")
    template_name = "concerts_app/artista_update.html"


# endregion
