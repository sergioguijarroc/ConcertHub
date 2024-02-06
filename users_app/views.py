from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DetailView, ListView
from concerts_app.models import Concierto
from tickets_app.models import Reserva

# Create your views here.


class ListarReservasUsuario(View):
    def get(self, request):
        reservas = Reserva.objects.filter(cliente_reserva=self.request.user)
        return render(
            request, "users_app/concierto_usuario_list.html", {"reservas": reservas}
        )
