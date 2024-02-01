from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DetailView
from .forms import ReservaForm,ComprobarVenta
from concerts_app.models import Concierto
from .models import Reserva

# Create your views here.


class ComprarEntradas(View):#Hay que meterle que esté logueado
    def get(self, request, pk):
        concierto = get_object_or_404(Concierto, pk=pk)
        formulario = ReservaForm()
        return render(
            request,
            "tickets_app/comprar_entradas.html",
            {"concierto": concierto, "formulario": formulario},
        )

    def post(self, request, pk):
        formulario = ReservaForm(request.POST)
        if formulario.is_valid():
            concierto = get_object_or_404(Concierto, pk=pk)
            unidades = formulario.cleaned_data["cantidad_tickets"]
            usuario = usuario.request()
            return redirect("tickets_app/confirmacion_compra.html",concierto,unidades,usuario)
        return render(
            request,
            "tickets_app/comprar_entradas.html",
            {"concierto": concierto, "formulario": formulario}
        )

class ConfirmacionCompra(View):
    def get(self,request, *args, **kwargs):
        concierto = kwargs["concierto",None]
        unidades = kwargs["unidades",None]
        usuario = kwargs["usuario",None]
        form = ComprobarVenta({"unidades":unidades})
        if form.is_valid():
            return render(request,"tickets_app/confirmacion_compra.html",{"concierto":concierto,"unidades":unidades,"usuario":usuario})
        
    def post(self,request):
        form = ComprobarVenta(request.POST)
        
        
        

        if usuario.saldo >= importeTotal:
            if unidades <= producto.unidades_stock:
                # Aplico el descuento al importe
                if promocion: # Si existe la promocion
                    if (
                        promocion.fecha_inicio
                        <= datetime.date.today()
                        <= promocion.fecha_fin
                    ):
                        importeTotal = importeTotal * (100 - promocion.descuento) / 100

                usuario.actualizarSaldoYTotalGastado(importeTotal)
                compra = Compra.objects.create(
                    usuario=usuario,
                    producto=producto,
                    unidades=unidades,
                    importe=importeTotal,
                )
                compra.sumarVentasProducto(unidades)
                producto.actualizarStock(unidades)

            return render(
                request,
                "tienda/compra_exito.html",
                {"compra": compra, "promocion": promocion},
            )
        else:
            return render(
                request, "tienda/comprar_producto.html", {"producto": producto}
            )
"""
