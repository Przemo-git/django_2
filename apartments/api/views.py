from rest_framework import viewsets
from ..models import Apartment, Owner
from .serializers import ApartmentSerializer

class ApertamentViewSet(viewsets.ModelViewSet):
    serializer_class = ApartmentSerializer
    queryset = Apartment.objects.all()

# class ApartmentDetailSet(viewsets.ModelViewSet):
#     serializer_class = ApartmentSerializer
#     queryset = Apartment.objects.get(id=id)
#     queryset2 = Owner.objects.get(id=id)