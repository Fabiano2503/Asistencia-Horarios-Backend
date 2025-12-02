from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

# Import correcto (tu carpeta está en minúsculas)
from apps.reportes.infrastructure import views


class ReportesAPITests(APITestCase):
    def setUp(self):
        # ESTO ES LO QUE ARREGLA TODO EL ERROR ".accepted_renderer not set"
        self.client = APIClient()
        # Forzamos JSON como renderer por defecto (el más común y rápido)
        self.client.default_format = 'json'
        # También puedes forzar headers si querés
        self.client.credentials(HTTP_ACCEPT='application/json')

    def test_dashboard_summary(self):
        url = reverse("reportes:summary")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_advertencias_mes_actual(self):
        url = reverse("reportes:advertencias_mes_actual")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_advertencias_historico(self):
        url = reverse("reportes:advertencias_historico")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_permisos_semana_actual(self):
        url = reverse("reportes:permisos_semana_actual")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_permisos_por_practicante(self):
        url = reverse("reportes:permisos_por_practicante")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_resumen_global_horas(self):
        url = reverse("reportes:resumen_global_horas")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_detalle_cumplimiento_horas(self):
        url = reverse("reportes:detalle_cumplimiento_horas")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_export_reporte_semanal(self):
        url = reverse("reportes:export_reporte_semanal")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Fix: el Content-Type real del Excel
        self.assertEqual(
            response.headers["Content-Type"],
            "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )

    def test_export_reporte_mensual(self):
        url = reverse("reportes:export_reporte_mensual")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class SmokeTest(TestCase):
    def test_importar_views(self):
        """Solo verifica que el módulo se importe sin errores"""
        try:
            import apps.reportes.infrastructure.views  # noqa: F401
        except Exception as e:
            self.fail(f"No se pudo importar views: {e}")
