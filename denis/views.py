from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    info = 'Мазур Денис Олегович'
    group = 'БИН-22-1'
    age = 22
    return HttpResponse(f'<h4>ФИО: {info}<h4>\n<h4>Группа: {group}<h4>\n<h4>Возраст: {age}<h4>')
