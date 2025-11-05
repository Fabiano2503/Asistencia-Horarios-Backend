from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .serializers import PracticanteSerializer, EstadisticasSerializer
from ..application.services import PracticanteService
from .repositories import DjangoPracticanteRepository

# ViewSet para el manejo de Practicantes
class PracticanteViewSet(viewsets.ModelViewSet):
    serializer_class = PracticanteSerializer
    practicante_service = PracticanteService(DjangoPracticanteRepository())

    # Obtener el queryset basado en filtros de consulta
    def get_queryset(self):
        nombre = self.request.query_params.get('nombre')
        correo = self.request.query_params.get('correo')
        estado = self.request.query_params.get('estado')

        if not nombre and not correo and not estado:
            return self.practicante_service.get_all_practicantes()

        return self.practicante_service.filter_practicantes(nombre, correo, estado)

    # Retrieve, List, Create, Update, Delete actions
    def retrieve(self, request, *args, **kwargs):
        instance = self.practicante_service.get_practicante_by_id(kwargs.get('pk'))
        if not instance:
            return Response({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        practicante = self.practicante_service.create_practicante(serializer.validated_data)
        serializer = self.get_serializer(practicante)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.practicante_service.get_practicante_by_id(kwargs.get('pk'))
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        practicante = self.practicante_service.update_practicante(kwargs.get('pk'), serializer.validated_data)
        return Response(self.get_serializer(practicante).data)

    def destroy(self, request, *args, **kwargs):
        self.practicante_service.delete_practicante(kwargs.get('pk'))
        return Response(status=status.HTTP_204_NO_CONTENT)

    # Acción personalizada para obtener estadísticas de practicantes
    @action(detail=False, methods=['get'])
    def estadisticas(self, request):
        stats = self.practicante_service.get_practicante_stats()
        serializer = EstadisticasSerializer(stats)
        return Response(serializer.data)
