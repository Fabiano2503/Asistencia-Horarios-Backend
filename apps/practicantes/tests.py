from django.test import TestCase
from .domain.models import Practicante
from .application.services import PracticanteService
from .infrastructure.repositories import DjangoPracticanteRepository

class PracticanteModelTest(TestCase):

    # Test el modelo Practicante
    def setUp(self):
        self.practicante = Practicante.objects.create(
            id_discord=123456789012345678,
            nombre='Test',
            apellido='User',
            correo='test.user@example.com',
            semestre=5,
            estado='activo'
        )

    def test_practicante_creation(self):
        self.assertIsInstance(self.practicante, Practicante)
        self.assertEqual(self.practicante.__str__(), 'Test User')

class PracticanteServiceTest(TestCase):

    # Test los servicios de Practicante
    def setUp(self):
        self.service = PracticanteService(DjangoPracticanteRepository())
        self.practicante1 = self.service.create_practicante({
            'id_discord': 1,
            'nombre': 'Juan',
            'apellido': 'Perez',
            'correo': 'juan.perez@test.com',
            'semestre': 5,
            'estado': 'activo'
        })
        self.practicante2 = self.service.create_practicante({
            'id_discord': 2,
            'nombre': 'Maria',
            'apellido': 'Gomez',
            'correo': 'maria.gomez@test.com',
            'semestre': 7,
            'estado': 'en_recuperacion'
        })

    def test_get_all_practicantes(self):
        practicantes = self.service.get_all_practicantes()
        self.assertEqual(len(practicantes), 2)

    def test_get_practicante_by_id(self):
        practicante = self.service.get_practicante_by_id(self.practicante1.id)
        self.assertEqual(practicante.nombre, 'Juan')

    def test_create_practicante(self):
        nuevo_practicante_data = {
            'id_discord': 3,
            'nombre': 'Pedro',
            'apellido': 'Lopez',
            'correo': 'pedro.lopez@test.com',
            'semestre': 3,
            'estado': 'en_riesgo'
        }
        practicante = self.service.create_practicante(nuevo_practicante_data)
        self.assertIsNotNone(practicante.id)
        self.assertEqual(practicante.nombre, 'Pedro')

    def test_update_practicante(self):
        update_data = {'nombre': 'Juanito'}
        practicante_actualizado = self.service.update_practicante(self.practicante1.id, update_data)
        self.assertEqual(practicante_actualizado.nombre, 'Juanito')

    def test_delete_practicante(self):
        self.service.delete_practicante(self.practicante1.id)
        practicante = self.service.get_practicante_by_id(self.practicante1.id)
        self.assertIsNone(practicante)

    def test_filter_practicantes(self):
        practicantes = self.service.filter_practicantes(nombre='Juan')
        self.assertEqual(len(practicantes), 1)
        self.assertEqual(practicantes[0].nombre, 'Juan')

    def test_get_practicante_stats(self):
        stats = self.service.get_practicante_stats()
        self.assertEqual(stats['total'], 2)
        self.assertEqual(stats['activos'], 1)
        self.assertEqual(stats['en_recuperacion'], 1)
        self.assertEqual(stats['en_riesgo'], 0)
