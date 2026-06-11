from rest_framework import serializers
from .models import Service, ServicePrice, ServicePromotion, Promotion

class ServicePriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServicePrice
        fields = ['id', 'name', 'price']

class PromotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promotion
        fields = ['id','title','description','image']

class ServiceCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id','title','slug','image']

class ServiceDetailSerializer(serializers.ModelSerializer):
    price = ServicePriceSerializer(many=True)
    promotion = serializers.SerializerMethodField()
    other_services = serializers.SerializerMethodField()

    class Meta:
        model = Service
        fields = ['id',
                  'title',
                  'description',
                  'slug',
                  'image',
                  'short_description',
                  'price',
                  'promotion',
                  'other_services'
                  ]
        def get_promotion(self, obj):
            promotions = Promotion.objects.filter(
                servicepromotion__service=obj
            )
            return PromotionSerializer(promotions, many=True).data
        
        def get_other_services(self, obj):
            services = Service.objects.exclude(id=obj.id)[:4]
            return ServiceCardSerializer(services, many=True).data