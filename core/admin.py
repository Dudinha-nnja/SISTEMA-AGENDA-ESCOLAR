from django.contrib import admin
from .models import Aluno, Professor, Disciplina, Agenda

admin.site.register(Aluno)
admin.site.register(Professor)
admin.site.register(Disciplina)
admin.site.register(Agenda)
