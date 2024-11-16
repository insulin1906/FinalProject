from rest_framework import viewsets
from .models import ProductQuery
from .serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = ProductQuery.objects.all()
    serializer_class = ProductSerializer

