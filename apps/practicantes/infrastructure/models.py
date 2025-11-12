from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Modelo que representa un practicante
class Practicante(models.Model):
    class Estado(models.TextChoices):
        ACTIVO = 'activo', 'Activo'
        EN_RECUPERACION = 'en_recuperacion', 'En Recuperación'
        EN_RIESGO = 'en_riesgo', 'En Riesgo'

    id_discord = models.BigIntegerField(unique=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    semestre = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(6)]) # Semestre entre 1 y 6
    estado = models.CharField(
        max_length=20,
        choices=Estado.choices,
        default=Estado.ACTIVO
    )

    def __str__(self):
        return f'{self.nombre} {self.apellido}'

# Modelo para practicantes en reforzamiento
class PracticanteReforzamiento(models.Model):
    class Estado(models.TextChoices):
        EN_REFORZAMIENTO = 'en_reforzamiento', 'En Reforzamiento'
        COMPLETADO = 'completado', 'Completado'
        REINTEGRADO = 'reintegrado', 'Reintegrado'

    practicante = models.ForeignKey(
        Practicante,
        on_delete=models.CASCADE,
        related_name='reforzamientos'
    )
    nombre_completo = models.CharField(max_length=200)
    area = models.CharField(max_length=100, default="Falta agregar")
    motivo = models.TextField(default="Falta agregar")
    fecha_ingreso = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(
        max_length=20,
        choices=Estado.choices,
        default=Estado.EN_REFORZAMIENTO
    )

    class Meta:
        db_table = 'practicantes_reforzamiento'
        verbose_name = 'Practicante en Reforzamiento'
        verbose_name_plural = 'Practicantes en Reforzamiento'
        ordering = ['-fecha_ingreso']

    def __str__(self):
        return f'{self.nombre_completo} - {self.area}'