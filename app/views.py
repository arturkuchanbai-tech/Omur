from rest_framework import generics
from .models import Услуга,Контакты
from .serializers import ServiceDetailSerializer,ServiceCardSerializer,ContactRequestSerializer

class ServiceListAPIView(generics.ListAPIView):
    queryset = Услуга.objects.filter(is_active=True).order_by('order')
    serializer_class = ServiceCardSerializer
    
class ServiceDetailAPIView(generics.RetrieveAPIView):
    queryset = Услуга.objects.filter(is_active=True)
    serializer_class = ServiceDetailSerializer
    lookup_field = 'slug'

class ContactRequestCreateAPIView(generics.CreateAPIView):
    queryset = Контакты.objects.all()
    serializer_class = ContactRequestSerializer