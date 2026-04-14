from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    whatsapp = models.CharField(max_length=20)
    perfil = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Professor(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Disciplina(models.Model):
    nome = models.CharField(max_length=100)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


class Agenda(models.Model):
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    aula = models.CharField(max_length=100)
    planejado = models.TextField()
    executado = models.TextField()
    tarefa_casa = models.TextField()

    def __str__(self):
        return self.disciplina.nome
    

from django.db import models

class Disciplina(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Agenda(models.Model):
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    aula = models.CharField(max_length=200)
    planejado = models.TextField()
    executado = models.TextField()
    tarefa_casa = models.TextField()

    def __str__(self):
        return self.aula