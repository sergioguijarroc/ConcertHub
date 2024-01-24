from django.urls import path
from . import views
from .views import Listar_conciertos

urlpatterns = [
    path("", views.index, name="index"),
    path("listar_conciertos", Listar_conciertos.as_view(), name="listar_conciertos"),
]
