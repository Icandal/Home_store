from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def index(request: HttpRequest) -> HttpResponse:
    context = {
        'title': 'Home',
        'content': 'Главная страница магазина HOME',
        'list': ['First', 'Second'],
        'dict': {'First': 1},
        'is_authenticated': False
    }


    return render(
        request=request, template_name='main/index.html', context=context #Иммитация подгрузки из базы данных
    )


def about(request: HttpRequest) -> HttpResponse:
    return HttpResponse('About page')