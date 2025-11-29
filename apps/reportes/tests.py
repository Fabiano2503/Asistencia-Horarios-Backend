# practicantes/tests.py
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class ReportesAPITests(APITestCase):
    """
    Tests completos para todos los endpoints del módulo de reportes
    """

    def test_dashboard_summary(self):
        url = reverse("reportes:summary")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("total_horas_semana", response.data)
        self.assertIn("practicantes_activos", response.data)
        self.assertIn("advertencias", response.data)
        self.assertIn("con_permiso", response.data)

    def test_advertencias_mes_actual(self):
        url = reverse("practicantes:warnings-current")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, list)

    def test_advertencias_historico(self):
        url = reverse("practicantes:warnings-history")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, list)

    def test_detalle_cumplimiento_horas(self):
        url = reverse("practicantes:compliance-detail")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, list)

    def test_resumen_global_horas(self):
        url = reverse("practicantes:global-summary")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("total_horas", response.data)

    def test_permisos_semana_actual(self):
        url = reverse("practicantes:permissions-week")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, list)

    def test_permisos_por_practicante(self):
        url = reverse("practicantes:permissions-employee")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, list)

    def test_export_reporte_semanal(self):
        url = reverse("practicantes:export-weekly")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.headers["Content-Type"],
            "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
        self.assertTrue(response.headers["Content-Disposition"].startswith("attachment; filename=reporte_semanal"))

    def test_export_reporte_mensual(self):
        url = reverse("practicantes:export-monthly")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.headers["Content-Disposition"].startswith("attachment; filename=reporte_mensual"))


# Test simple de smoke (opcional, para CI/CD)
class SmokeTest(TestCase):
    def test_import_views(self):
        """Asegura que todos los views se importan sin errores"""
        try:
            from practicantes.views import (
                dashboard_summary,
                advertencias_mes_actual,
                advertencias_historico,
                detalle_cumplimiento_horas,
                resumen_global_horas,
                permisos_semana_actual,
                permisos_por_practicante,
                export_reporte_semanal,
                export_reporte_mensual,
            )
            self.assertTrue(True)
        except ImportError as e:
            self.fail(f"Error al importar views: {e}")