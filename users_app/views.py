from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DetailView, ListView
from concerts_app.models import Concierto
from tickets_app.models import Reserva
from .models import Reserva

# Create your views here.


class ListarReservasUsuario(ListView):
    model = Reserva
    template_name = "concierto_usuario_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["reservas"] = Reserva.objects.filter(cliente_reserva=self.user)
        return context
