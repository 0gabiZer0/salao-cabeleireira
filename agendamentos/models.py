from django.db import models


class Agendamento(models.Model):
    SERVICOS = [
        ('Corte', 'Corte'),
        ('Escova', 'Escova'),
        ('Coloração', 'Coloração'),
        ('Hidratação', 'Hidratação'),
        ('Progressiva', 'Progressiva'),
        ('Penteado', 'Penteado'),
    ]

    nome = models.CharField(max_length=100)
    contato = models.CharField(max_length=20)
    data = models.DateField()
    servico = models.CharField('serviço', max_length=20, choices=SERVICOS)

    def __str__(self):
        return f'{self.nome} - {self.servico}'
