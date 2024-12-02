from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Corporation


# Create your views here.
def stocks_list(request):
    corporations = Corporation.objects.all()
    return render(request, "stocks/index.html", {"corporations": corporations})


def detail(request, corporation_ticker):
    corporation = get_object_or_404(Corporation, ticker=corporation_ticker.upper())
    return render(request, "stocks/detail.html", {"corporation": corporation})
