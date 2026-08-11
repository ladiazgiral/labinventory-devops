from django.db import models


class Equipo(models.Model):

    ESTADOS = [
        ("disponible", "Disponible"),
        ("prestado", "Prestado"),
        ("mantencion", "Mantención"),
        ("baja", "Baja"),
    ]

    nombre = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    numero_serie = models.CharField(max_length=100, unique=True)

    estado = models.CharField(
        max_length=20,
        choices=ESTADOS,
        default="disponible"
    )

    ubicacion = models.CharField(max_length=150)

    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} - {self.numero_serie}"