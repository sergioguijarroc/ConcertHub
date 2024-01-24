from django.urls import path
from . import views
from .views import ConciertoListView

urlpatterns = [
    path("", views.index, name="index"),
    path("listar_conciertos", ConciertoListView.as_view(), name="listar_conciertos"),
]
