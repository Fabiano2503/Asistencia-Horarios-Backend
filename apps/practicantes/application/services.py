from typing import List, Optional
from datetime import datetime
from apps.practicantes.domain.practicante import Practicante, EstadoPracticante
from apps.practicantes.domain.repositories import PracticanteRepository, ReforzamientoRepository
from apps.practicantes.domain.reforzamiento import PracticanteReforzamiento, EstadoReforzamiento  

# Clase de servicio para gestionar la lógica de negocio relacionada con los practicantes
class PracticanteService:

    def __init__(self, practicante_repository: PracticanteRepository, reforzamiento_repository: ReforzamientoRepository = None):
        self.practicante_repository = practicante_repository
        self.reforzamiento_repository = reforzamiento_repository

    def get_all_practicantes(self) -> List[Practicante]:
        return self.practicante_repository.get_all()

    def get_practicante_by_id(self, practicante_id: int) -> Optional[Practicante]:
        return self.practicante_repository.get_by_id(practicante_id)

    def create_practicante(self, practicante_data: dict) -> Practicante:
        practicante = Practicante(**practicante_data)
        return self.practicante_repository.create(practicante)

    def update_practicante(self, practicante_id: int, practicante_data: dict) -> Optional[Practicante]:
        practicante = self.get_practicante_by_id(practicante_id)
        if practicante:
            # Guardar el estado anterior
            estado_anterior = practicante.estado
            
            for key, value in practicante_data.items():
                if key == 'estado':
                    setattr(practicante, key, EstadoPracticante(value))
                else:
                    setattr(practicante, key, value)
            
            practicante_actualizado = self.practicante_repository.update(practicante)
            
            # NUEVO: Si cambió a estado EN_RECUPERACION, crear automáticamente el reforzamiento
            if (estado_anterior != EstadoPracticante.EN_RECUPERACION and 
                practicante_actualizado.estado == EstadoPracticante.EN_RECUPERACION and
                self.reforzamiento_repository is not None):
                
                # Verificar si ya existe un registro de reforzamiento
                reforzamiento_existente = self.reforzamiento_repository.get_by_practicante_id(practicante_id)
                
                if not reforzamiento_existente:
                    # Crear automáticamente el registro de reforzamiento
                    reforzamiento = PracticanteReforzamiento(
                        practicante_id=practicante_actualizado.id,
                        nombre_completo=practicante_actualizado.nombre_completo,
                        area="Falta agregar",
                        motivo="Falta agregar",
                        fecha_ingreso=datetime.now(),
                        estado=EstadoReforzamiento.EN_REFORZAMIENTO
                    )
                    self.reforzamiento_repository.create(reforzamiento)
            
            return practicante_actualizado
        return None

    def delete_practicante(self, practicante_id: int) -> None:
        self.practicante_repository.delete(practicante_id)

    def filter_practicantes(self, nombre: Optional[str] = None, correo: Optional[str] = None, estado: Optional[str] = None) -> List[Practicante]:
        return self.practicante_repository.filter(nombre, correo, estado)

    def get_practicante_stats(self) -> dict[str, int]:
        return self.practicante_repository.get_stats()


# Servicio de aplicación para reforzamiento
class ReforzamientoService:

    def __init__(self, reforzamiento_repository: ReforzamientoRepository, practicante_repository: PracticanteRepository):
        self.reforzamiento_repository = reforzamiento_repository
        self.practicante_repository = practicante_repository

    def get_all_reforzamientos(self) -> List[PracticanteReforzamiento]:
        return self.reforzamiento_repository.get_all()

    def get_reforzamiento_by_id(self, reforzamiento_id: int) -> Optional[PracticanteReforzamiento]:
        return self.reforzamiento_repository.get_by_id(reforzamiento_id)

    def crear_reforzamiento_desde_practicante(self, practicante_id: int) -> Optional[PracticanteReforzamiento]:
        practicante = self.practicante_repository.get_by_id(practicante_id)
        
        if not practicante:
            return None
        
        if practicante.estado != EstadoPracticante.EN_RECUPERACION:
            return None
        
        reforzamiento_existente = self.reforzamiento_repository.get_by_practicante_id(practicante_id)
        if reforzamiento_existente:
            return reforzamiento_existente
        
        reforzamiento = PracticanteReforzamiento(
            practicante_id=practicante.id,
            nombre_completo=practicante.nombre_completo,
            area="Falta agregar",
            motivo="Falta agregar",
            fecha_ingreso=datetime.now(),
            estado=EstadoReforzamiento.EN_REFORZAMIENTO
        )
        
        return self.reforzamiento_repository.create(reforzamiento)

    def actualizar_area_motivo(self, reforzamiento_id: int, area: Optional[str] = None, motivo: Optional[str] = None) -> Optional[PracticanteReforzamiento]:
        reforzamiento = self.get_reforzamiento_by_id(reforzamiento_id)
        
        if not reforzamiento:
            return None
        
        reforzamiento.actualizar_informacion(area, motivo)
        return self.reforzamiento_repository.update(reforzamiento)

    def marcar_como_completado(self, reforzamiento_id: int) -> Optional[PracticanteReforzamiento]:
        reforzamiento = self.get_reforzamiento_by_id(reforzamiento_id)
        
        if not reforzamiento:
            return None
        
        reforzamiento.marcar_completado()
        return self.reforzamiento_repository.update(reforzamiento)

    def marcar_como_reintegrado(self, reforzamiento_id: int) -> Optional[PracticanteReforzamiento]:
        reforzamiento = self.get_reforzamiento_by_id(reforzamiento_id)
        
        if not reforzamiento:
            return None
        
        reforzamiento.marcar_reintegrado()
        return self.reforzamiento_repository.update(reforzamiento)

    def get_metricas(self) -> dict:
        return self.reforzamiento_repository.get_metricas()

    def filter_by_estado(self, estado: str) -> List[PracticanteReforzamiento]:
        return self.reforzamiento_repository.filter_by_estado(estado)