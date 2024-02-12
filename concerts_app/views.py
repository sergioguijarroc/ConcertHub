from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    UpdateView,
    DeleteView,
)
from .models import Concierto, Artista
from .forms import ArtistaForm, ConciertoForm
from tickets_app.models import Reserva, Valoracion
from django.db.models import Sum

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


class ConciertoReview(View):
    def get(self, request, pk):
        concierto = get_object_or_404(Concierto, pk=pk)
        return render(
            request,
            "concerts_app/conciertos/concierto_review.html",
            {"concierto": concierto},
        )

    def post(self, request, pk):
        reserva = Reserva.objects.get(pk=pk)
        concierto = Concierto.objects.get(pk=reserva.concierto_reserva.pk)
        valoracionUsuario = float(request.POST["valoracion"])

        if (
            # reserva.cliente_reserva == request.user and
            valoracionUsuario >= 0
            and valoracionUsuario <= 10
        ):
            if reserva.valoracion_usuario is not None:
                reserva.valoracion_usuario.actualizar_rating(valoracionUsuario)
                reserva.valoracion_usuario.save()
                reserva.save()
            else:
                valoracion = Valoracion.objects.create(
                    reserva_valoracion=reserva,
                    usuario_valoracion=request.user,
                    rating=valoracionUsuario,
                )
                reserva.valoracion_usuario = valoracion
                reserva.save()
                valoracion.save()

            concierto.actualizar_valoracion_media()
            concierto.save()

        return redirect("listar_reservas_usuario")


class ListarConciertosMasVendidos(ListView):
    model = Reserva
    template_name = "concerts_app/conciertos/concierto_top_ventas.html"

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        top_conciertos_ventas = (
            Reserva.objects.values(
                "concierto_reserva"
            )  # Accedo a todas las reservas y obtengo el valor de concierto_reserva de cada uno
            .annotate(
                sum_compras=Sum("cantidad_tickets")
            )  # Sumo la cantidad de tickets de cada concierto
            .order_by("-sum_compras")[
                :3
            ]  # Ordeno de mayor a menor (con el -) y me quedo con los 3 primeros
        )
        context["conciertos_top_ventas"] = top_conciertos_ventas
        return context


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
    form_class = ArtistaForm
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
