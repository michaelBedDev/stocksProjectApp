from django.shortcuts import render, redirect
from django.http import HttpResponseBadRequest
from .models import Investment

# Create your views here.


def portfolio(request):
    investments = Investment.objects.all()
    return render(request, "investments/index.html", {"investments": investments})


from django.shortcuts import render, redirect
from django.http import HttpResponseBadRequest
from .models import Investment


from django.shortcuts import render
from django.http import HttpResponseBadRequest
from .models import Investment


def portfolio(request):
    if request.method == "POST":
        # Procesar el formulario de nueva inversión
        ticker_name = request.POST.get("ticker_name")
        stocks_amount = request.POST.get("stocks_amount")
        price_at_purchase = request.POST.get("price_at_purchase")

        # Validación básica
        if not ticker_name or not stocks_amount or not price_at_purchase:
            return HttpResponseBadRequest("Todos los campos son obligatorios.")

        try:
            # Crear nueva inversión
            Investment.objects.create(
                ticker_name=ticker_name,
                stocks_amount=stocks_amount,
                price_at_purchase=price_at_purchase,
            )
        except Exception as e:
            return HttpResponseBadRequest(f"Error al guardar la inversión: {e}")

    # Recuperar todas las inversiones para mostrarlas en la página
    investments = Investment.objects.all()
    return render(request, "investments/index.html", {"investments": investments})
