from rest_framework import generics
from .models import Service, ContactRequest
from .serializers import ServiceDetailSerializer,ServiceCardSerializer,ContactRequestSerializer

class ServiceListAPIView(generics.ListAPIView):
    queryset = Service.objects.filter(is_active=True).order_by('order')
    serializer_class = ServiceCardSerializer
    
class ServiceDetailAPIView(generics.RetrieveAPIView):
    queryset = Service.objects.filter(is_active=True)
    serializer_class = ServiceDetailSerializer
    lookup_field = 'slug'

class ContactRequestCreateAPIView(generics.CreateAPIView):
    queryset = ContactRequest.objects.all()
    serializer_class = ContactRequestSerializer