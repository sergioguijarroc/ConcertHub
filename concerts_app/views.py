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
    template_name = "concerts_app/conciertos/concierto_detail.html"


# Staff
class ConciertoCreateView(CreateView):
    model = Concierto
    fields = [  # Le paso todos menos boletos_disponibles porque se calcula en el modelo
        "nombre",
        "artista_concierto",
        "ubicacion_concierto",
        "fecha",
        "precio_entrada",
        "descripcion",
        "foto",
    ]
    success_url = reverse_lazy("concierto_list")
    template_name = "concerts_app/conciertos/concierto_create.html"


class ConciertoDeleteView(DeleteView):
    model = Concierto
    success_url = reverse_lazy("concierto_list")
    template_name = "concerts_app/conciertos/concierto_confirm_delete.html"


class ConciertoUpdateView(UpdateView):
    model = Concierto
    fields = [
        "nombre",
        "artista_concierto",
        "ubicacion_concierto",
        "fecha",
        "precio_entrada",
        "descripcion",
        "foto",
    ]
    success_url = reverse_lazy("concierto_list")
    template_name = "concerts_app/conciertos/concierto_update.html"


# endregion
# region Artistas


# Usuarios normales
class ArtistaListView(ListView):
    model = Artista
    template_name = "concerts_app/artistas/artista_list.html"


class ArtistaDetailView(DetailView):
    model = Artista
    template_name = "concerts_app/artistas/artista_detail.html"


# Staff
class ArtistaCreateView(CreateView):
    model = Artista
    fields = "__all__"
    success_url = reverse_lazy("concierto_list")
    template_name = "concerts_app/artistas/artista_create.html"


class ArtistaDeleteView(DeleteView):
    model = Artista
    success_url = reverse_lazy("artista_list")
    template_name = "concerts_app/artistas/artista_confirm_delete.html"


class ArtistaUpdateView(UpdateView):
    model = Artista
    fields = "__all__"
    success_url = reverse_lazy("concierto_list")
    template_name = "concerts_app/artista_update.html"
    template_name = "concerts_app/artistas/artista_update.html"


# endregion
