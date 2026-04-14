from django.shortcuts import render
from .models import Agenda

def home(request):
    tarefas = Agenda.objects.all()
    return render(request, 'home.html', {'tarefas': tarefas})