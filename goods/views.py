from django.http import HttpResponse
from django.shortcuts import render

from goods.models import Products


def catalog(request) -> HttpResponse:

    goods = Products.objects.all()

    context = {
        "title": "Home - Каталог",
        "goods": goods,
        }
    return render(request=request, template_name="goods/catalog.html", context=context)


def product(request) -> HttpResponse:

    return render(request=request, template_name="goods/product.html")
