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

    class Meta:
        db_table = "practicante"
        verbose_name = "Practicante"
        verbose_name_plural = "Practicantes"

    def __str__(self):
        return f'{self.nombre} {self.apellido}'

class Asistencia(models.Model):
    practicante = models.ForeignKey(Practicante, on_delete=models.CASCADE, related_name='asistencias')
    fecha = models.DateField()
    hora_entrada = models.TimeField()
    hora_salida = models.TimeField(null=True, blank=True)

    class Meta:
        db_table = 'asistencia'
        verbose_name = 'Asistencia'
        verbose_name_plural = 'Asistencias'
        unique_together = (('practicante', 'fecha'),)

class Horario(models.Model):
    DIAS_SEMANA = [
        ('lunes', 'Lunes'),
        ('martes', 'Martes'),
        ('miercoles', 'Miércoles'),
        ('jueves', 'Jueves'),
        ('viernes', 'Viernes'),
        ('sabado', 'Sábado'),
        ('domingo', 'Domingo'),
    ]
    practicante = models.ForeignKey(Practicante, on_delete=models.CASCADE, related_name='horarios')
    dia_semana = models.CharField(max_length=10, choices=DIAS_SEMANA)
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()

    class Meta:
        db_table = 'horario'
        verbose_name = 'Horario'
        verbose_name_plural = 'Horarios'
        unique_together = (('practicante', 'dia_semana', 'hora_inicio'),)

class Advertencia(models.Model):
    TIPO_CHOICES = [
        ('retraso', 'Retraso'),
        ('falta', 'Falta'),
        ('inasistencia', 'Inasistencia'),
        ('otro', 'Otro'),
    ]
    GRAVEDAD_CHOICES = [
        ('leve', 'Leve'),
        ('moderada', 'Moderada'),
        ('grave', 'Grave'),
    ]
    practicante = models.ForeignKey(Practicante, on_delete=models.CASCADE, related_name='advertencias')
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    gravedad = models.CharField(max_length=20, choices=GRAVEDAD_CHOICES, default='leve')
    descripcion = models.TextField()
    fecha = models.DateField(auto_now_add=True)
    resuelta = models.BooleanField(default=False)
    fecha_resolucion = models.DateField(null=True, blank=True)

    class Meta:
        db_table = 'advertencia'
        verbose_name = 'Advertencia'
        verbose_name_plural = 'Advertencias'
        ordering = ['-fecha']
