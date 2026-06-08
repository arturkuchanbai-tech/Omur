from django.urls import path,include
from .views import ServiceDetailViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'detail', ServiceDetailViewSet ,basename='services')


urlpatterns = [
    path('', include(router.urls)),

]
