from django.http import HttpResponse
from django.shortcuts import render


def catalog(request) -> HttpResponse:
    context = {
        "title": "Home - Каталог",
        }
    return render(request=request, template_name="goods/catalog.html", context=context)


def product(request) -> HttpResponse:

    return render(request=request, template_name="goods/product.html")
