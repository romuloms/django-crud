from django.db import models


class Usuario(models.Model):
    cpf = models.CharField(max_length=11, unique=True)
    nome = models.CharField(max_length=70)
    data_nascimento = models.DateField()

    def __str__(self):
        return self.nome