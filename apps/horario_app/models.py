# models.py
from django.db import models

DIAS_SEMANA = [
    ('Lunes', 'Lunes'),
    ('Martes', 'Martes'),
    ('Miércoles', 'Miércoles'),
    ('Jueves', 'Jueves'),
    ('Viernes', 'Viernes'),
    ('Sábado', 'Sábado'),
    ('Domingo', 'Domingo'),
]

class HorarioClase(models.Model):
    practicante = models.ForeignKey(
        'Practicante',
        on_delete=models.CASCADE,
        related_name='horarios_clase'
    )
    dia_clase = models.CharField(
        max_length=15,
        choices=DIAS_SEMANA,
        verbose_name="Día de clase"
    )
    dia_recuperacion = models.CharField(
        max_length=15,
        choices=DIAS_SEMANA,
        null=True,
        blank=True,
        verbose_name="Día de recuperación"
    )

    class Meta:
        db_table = 'horario_clases'
        unique_together = ('practicante', 'dia_clase')
        verbose_name = 'Horario de clase'
        verbose_name_plural = 'Horarios de clases'

    def __str__(self):
        rec = f" → {self.dia_recuperacion}" if self.dia_recuperacion else ""
        return f"{self.practicante} - {self.dia_clase}{rec}"