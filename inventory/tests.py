from rest_framework.test import APITestCase
from rest_framework import status

from .models import Equipo


class LabInventoryAPITests(APITestCase):

    def setUp(self):
        self.equipo = Equipo.objects.create(
            nombre="Router Cisco",
            categoria="Networking",
            marca="Cisco",
            modelo="ISR 4331",
            numero_serie="RTR-001",
            estado="disponible",
            ubicacion="Laboratorio Redes"
        )

    def test_health_endpoint(self):
        response = self.client.get("/api/health/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["status"], "ok")

    def test_version_endpoint(self):
        response = self.client.get("/api/version/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["version"], "1.0.0")

    def test_list_equipos(self):
        response = self.client.get("/api/equipos/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_equipo(self):
        response = self.client.get(
            f"/api/equipos/{self.equipo.id}/"
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_create_equipo(self):
        data = {
            "nombre": "Arduino UNO",
            "categoria": "IoT",
            "marca": "Arduino",
            "modelo": "UNO R3",
            "numero_serie": "ARD-001",
            "estado": "disponible",
            "ubicacion": "Laboratorio IoT"
        }

        response = self.client.post(
            "/api/equipos/",
            data,
            format="json"
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

    def test_update_equipo(self):
        data = {
            "nombre": "Router Cisco Actualizado",
            "categoria": "Networking",
            "marca": "Cisco",
            "modelo": "ISR 4331",
            "numero_serie": "RTR-001",
            "estado": "mantencion",
            "ubicacion": "Laboratorio Redes"
        }

        response = self.client.put(
            f"/api/equipos/{self.equipo.id}/",
            data,
            format="json"
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_delete_equipo(self):
        response = self.client.delete(
            f"/api/equipos/{self.equipo.id}/"
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

    def test_invalid_equipo(self):
        data = {
            "nombre": "",
            "categoria": "",
            "marca": "",
            "modelo": "",
            "numero_serie": "",
            "estado": "incorrecto",
            "ubicacion": ""
        }

        response = self.client.post(
            "/api/equipos/",
            data,
            format="json"
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )