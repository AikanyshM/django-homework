from django.shortcuts import render
from django.http import HttpResponse


def hello_world(request):
    return HttpResponse("Приветствуем Вас!")
def form(request):
    return render(request, 'form.html')

    
