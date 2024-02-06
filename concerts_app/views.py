from typing import Any
from django.http import HttpRequest, HttpResponse
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
from .forms import ConciertoForm

# Create your views here.


def index(request):
    return render(request, "concerts_app/panelControl.html")


# region Conciertos


class ListarConciertosUsuario(ListView):
    model = Concierto
    template_name = "concerts_app/"


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
    form_class = ConciertoForm
    success_url = reverse_lazy("concierto_list")
    template_name = "concerts_app/conciertos/concierto_create.html"

    def form_valid(
        self, form
    ):  # Se sobreescribe el método para que se pueda modificar el número de boletos disponibles
        concierto = form.save(
            commit=False
        )  # Con esto evitamos que se guarde el concierto hasta que se modifique el número de boletos disponibles, pero me lo traigo a la vista para modificarlo
        concierto.boletos_disponibles = concierto.ubicacion_concierto.capacidad
        concierto.save()
        return super().form_valid(
            form
        )  # Se guarda el concierto personalizado con el número de boletos disponibles modificado,se llama al método de la clase padre para que guarde el concierto


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
