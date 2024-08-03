from django.http import HttpResponse
from django.shortcuts import render, reverse
import datetime
import os


def home_view(request):
    template_name = 'app/home.html'
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('current_time'),
        'Показать содержимое рабочей директории': reverse ('workdir')
    }


    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def current_time_view(request):
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    msg = f'Текущее время: {current_time}'
    return HttpResponse(msg)


def workdir_view(request):
    files = os.listdir('.')
    msg = '<br>'.join(files)
    return HttpResponse(msg)
