from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    UpdateView,
    DeleteView,
)
from .models import Concierto

# Create your views here.


def index(request):
    return render(request, "concerts_app/panelControl.html")


# Usuarios normales


class ConciertoListView(ListView):
    model = Concierto


class ConciertoDetailView(DetailView):
    model = Concierto


# Staff
class ConciertoCreateView(CreateView):
    model = Concierto
    fields = "__all__"
    success_url = reverse_lazy("concierto_list")
    template_name = "concerts_app/concierto_create.html"


class ConciertoDeleteView(DeleteView):
    model = Concierto
    success_url = reverse_lazy("concierto_list")


class ConciertoUpdateView(UpdateView):
    model = Concierto
    fields = "__all__"
    success_url = reverse_lazy("concierto_list")
    template_name = "concerts_app/concierto_update.html"
