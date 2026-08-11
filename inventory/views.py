from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Equipo
from .serializers import EquipoSerializer


class EquipoViewSet(viewsets.ModelViewSet):

    queryset = Equipo.objects.all().order_by("-fecha_registro")

    serializer_class = EquipoSerializer


@api_view(["GET"])
def health(request):

    return Response({
        "status": "ok"
    })


@api_view(["GET"])
def version(request):

    return Response({
        "name": "LabInventory API",
        "version": "1.0.0"
    })
