from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView

# Create your views here.


def index(request):
    return render(request, "core_app/index.html")
