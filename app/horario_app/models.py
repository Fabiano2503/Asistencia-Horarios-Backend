from django.db import models

class Practicante(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Servidor(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Horario(models.Model):
    practicante = models.ForeignKey(Practicante, on_delete=models.CASCADE)
    servidor = models.ForeignKey(Servidor, on_delete=models.CASCADE)
    dia = models.CharField(max_length=20)
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    estado = models.CharField(max_length=20, default='pendiente')

    def __str__(self):
        return f"{self.practicante} - {self.dia}"