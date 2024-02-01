from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import ComprarEntradas
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path(
        "comprar_entradas/<int:pk>",
        login_required(ComprarEntradas.as_view()),
        name="comprar_entradas",
    ),
]
