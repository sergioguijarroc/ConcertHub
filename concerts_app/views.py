from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView
from .models import Concierto

# Create your views here.


def index(request):
    return render(request, "concerts_app/index.html")


class ConciertoListView(ListView):
    model = Concierto


class ConciertoDetailView(DetailView):
    model = Concierto
    template_name = "TEMPLATE_NAME"


class ConciertoCreateView(CreateView):
    model = Concierto
    template_name = "TEMPLATE_NAME"
