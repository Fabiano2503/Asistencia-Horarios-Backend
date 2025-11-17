from django.contrib import admin
from .models import Practicante, Servidor, Horario

@admin.register(Practicante)
class PracticanteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')

@admin.register(Servidor)
class ServidorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')

@admin.register(Horario)
class HorarioAdmin(admin.ModelAdmin):
    # ← USA LOS MÉTODOS, NO LOS CAMPOS
    list_display = ('id', 'get_practicante', 'get_servidor', 'dia', 'hora_inicio', 'hora_fin', 'estado')

    def get_practicante(self, obj):
        return obj.practicante.nombre
    get_practicante.short_description = 'Practicante'

    def get_servidor(self, obj):
        return obj.servidor.nombre
    get_servidor.short_description = 'Servidor'