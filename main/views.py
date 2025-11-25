from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from goods.models import Categories

def index(request: HttpRequest) -> HttpResponse:



    context = {"title": "Home - Главная", "content": "Магазин мебели HOME"}

    return render(
        request=request,
        template_name="main/index.html",
        context=context,  # Иммитация подгрузки из базы данных
    )


def about(request: HttpRequest) -> HttpResponse:
    context = {
        "title": "Home - О нас",
        "content": "О нас",
        "text_on_page": "Текст о чем-то про магазин и товар.",
    }

    return render(
        request=request,
        template_name="main/about.html",
        context=context,  # Иммитация подгрузки из базы данных
    )
