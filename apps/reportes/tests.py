from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

# RUTA CORRECTA A TUS VIEWS (ajustá si tu carpeta se llama "reportes" o "Reportes")
from apps.reportes.infrastructure import views


class ReportesAPITests(APITestCase):
    """
    Tests completos para todos los endpoints del módulo Reportes
    """

    def test_dashboard_summary(self):
        url = reverse("reportes:summary")  # ← nombre del name= en urls.py
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("total_horas_semana", response.data)
        self.assertIn("practicantes_activos", response.data)
        self.assertIn("advertencias", response.data)
        self.assertIn("con_permiso", response.data)

    def test_advertencias_mes_actual(self):
        url = reverse("reportes:warnings-current")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, list)

    def test_advertencias_historico(self):
        url = reverse("reportes:warnings-history")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, list)

    def test_detalle_cumplimiento_horas(self):
        url = reverse("reportes:compliance-detail")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, list)

    def test_resumen_global_horas(self):
        url = reverse("reportes:global-summary")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("total_horas", response.data)

    def test_permisos_semana_actual(self):
        url = reverse("reportes:permissions-week")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, list)

    def test_permisos_por_practicante(self):
        url = reverse("reportes:permissions-employee")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, list)

    def test_export_reporte_semanal(self):
        url = reverse("reportes:export-weekly")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.headers["Content-Type"],
            "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
        self.assertTrue(
            response.headers["Content-Disposition"].startswith("attachment; filename=")
        )

    def test_export_reporte_mensual(self):
        url = reverse("reportes:export-monthly")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(
            response.headers["Content-Disposition"].startswith("attachment; filename=")
        )


# Test de humo (smoke test) para CI/CD
class SmokeTest(TestCase):
    def test_importar_views_sin_errores(self):
        """Asegura que todas las views se importan correctamente"""
        try:
            _ = (
                views.dashboard_summary,
                views.advertencias_mes_actual,
                views.advertencias_historico,
                views.detalle_cumplimiento_horas,
                views.resumen_global_horas,
                views.permisos_semana_actual,
                views.permisos_por_practicante,
                views.export_reporte_semanal,
                views.export_reporte_mensual,
            )
            # Si llega aquí → todo se importó bien
        except Exception as e:
            self.fail(f"Falló al importar las views del módulo Reportes: {e}")
