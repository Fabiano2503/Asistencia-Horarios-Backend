from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from src.application.use_cases.registrar_horario import RegistrarHorarioUseCase
from src.domain.ports.horario_repository import HorarioRepository
from horario_app.models import Practicante, Servidor, Horario as HorarioModel
from src.domain.entities.horario import Horario

# --- IMPLEMENTACIÓN DEL REPOSITORIO ---
class HorarioRepositoryImpl(HorarioRepository):
    def save(self, horario: Horario) -> Horario:
        model = HorarioModel(
            practicante=horario.practicante,
            servidor=horario.servidor,
            dia=horario.dia,
            hora_inicio=horario.hora_inicio,
            hora_fin=horario.hora_fin
        )
        model.save()
        horario.id = model.id
        return horario

    def find_all(self, servidor_id=None):
        qs = HorarioModel.objects.all()
        if servidor_id:
            qs = qs.filter(servidor_id=servidor_id)
        return [self._to_entity(h) for h in qs]

    def find_pendientes(self):
        return [self._to_entity(h) for h in HorarioModel.objects.filter(estado='pendiente')]

    def find_by_practicante(self, practicante_id):
        return [self._to_entity(h) for h in HorarioModel.objects.filter(practicante_id=practicante_id)]

    def _to_entity(self, model):
        return Horario(
            id=model.id,
            practicante=model.practicante,
            servidor=model.servidor,
            dia=model.dia,
            hora_inicio=model.hora_inicio.strftime("%H:%M"),
            hora_fin=model.hora_fin.strftime("%H:%M")
        )

# Instancia del repositorio
repository = HorarioRepositoryImpl()

# --- VISTAS ---
class HorarioAPI(APIView):
    def post(self, request):
        print("Datos recibidos:", request.data)

        # Validar practicante y servidor
        try:
            practicante = Practicante.objects.get(id=request.data['practicante_id'])
            servidor = Servidor.objects.get(id=request.data['servidor_id'])
        except Practicante.DoesNotExist:
            return Response({"error": "Practicante no encontrado"}, status=400)
        except Servidor.DoesNotExist:
            return Response({"error": "Servidor no encontrado"}, status=400)

        # Preparar datos para el use case
        data = {
            'practicante': practicante,
            'servidor': servidor,
            'dia': request.data['dia'],
            'hora_inicio': request.data['hora_inicio'],
            'hora_fin': request.data['hora_fin']
        }

        # Ejecutar use case
        use_case = RegistrarHorarioUseCase(repository)
        horario = use_case.execute(data)

        # Respuesta
        return Response({
            "id": horario.id,
            "practicante": horario.practicante.nombre,
            "servidor": horario.servidor.nombre,
            "dia": horario.dia,
            "hora_inicio": horario.hora_inicio,
            "hora_fin": horario.hora_fin,
            "mensaje": "Horario guardado con Clean Architecture"
        }, status=status.HTTP_201_CREATED)

    def get(self, request):
        horarios = repository.find_all()
        data = [
            {
                "id": h.id,
                "practicante": h.practicante.nombre,
                "servidor": h.servidor.nombre,
                "dia": h.dia,
                "hora_inicio": h.hora_inicio,
                "hora_fin": h.hora_fin
            }
            for h in horarios
        ]
        return Response(data, status=200)


class PracticantesAPI(APIView):
    def get(self, request):
        practicantes = Practicante.objects.all()
        data = [{"id": p.id, "nombre": p.nombre} for p in practicantes]
        return Response(data)


class PendientesAPI(APIView):
    def get(self, request):
        horarios = repository.find_pendientes()
        data = [
            {
                "id": h.id,
                "practicante": h.practicante.nombre,
                "dia": h.dia,
                "hora_inicio": h.hora_inicio,
                "hora_fin": h.hora_fin
            }
            for h in horarios
        ]
        return Response(data)
    