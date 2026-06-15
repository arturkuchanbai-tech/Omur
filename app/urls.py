from django.urls import path
from .views import ServiceListAPIView,ServiceDetailAPIView,ContactRequestCreateAPIView


urlpatterns = [
    path('services/', ServiceListAPIView.as_view(), name='service-list'),
    path('services/<slug:slug>/', ServiceDetailAPIView.as_view(), name='service-detail'),
    path('contact/', ContactRequestCreateAPIView.as_view(), name='contact-request'),
]
