from django.urls import path
from .views import ServiceListAPIView,ServiceDetailAPIView,ContactRequestCreateAPIView


urlpatterns = [
    path('Услуги/', ServiceListAPIView.as_view(), name='service-list'),
    path('Услуги/<slug:slug>/', ServiceDetailAPIView.as_view(), name='service-detail'),
    path('Контакт/', ContactRequestCreateAPIView.as_view(), name='contact-request'),
]
