from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny
from .models import Tarea
from .serializers import TareaSerializer

class TareaViewSet(viewsets.ModelViewSet):
    """
    Permite: GET (lista/detalle), POST (crear), PATCH (parcial), DELETE (borrar).
    """
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer
    permission_classes = [AllowAny]
