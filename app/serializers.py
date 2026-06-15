from rest_framework import serializers
from .models import Service, ServicePrice, ServicePromotion, Promotion, Review, Doctor, ContactRequest

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

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id',
                  'author',
                  'text',
                  'video',
                  'photo',
                  'created_at'
                  ]

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['id',
                  'full_name',
                  'specialty',
                  'photo',
                  'description'
                  ]
        
class ContactRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactRequest
        fields = ['id',
                  'name',
                  'phone',
                  'created_at'
                  ]
        
class ServiceDetailSerializer(serializers.ModelSerializer):
    prices = ServicePriceSerializer(many=True, read_only=True)
    doctors = DoctorSerializer(many=True, read_only=True)
    reviews = ReviewSerializer(many=True, read_only=True)
    promotion = serializers.SerializerMethodField()
    other_services = serializers.SerializerMethodField()

    class Meta:
        model = Service
        fields = ['id',
                  'meta_title',
                  'meta_description',
                  'slug',
                  'image',
                  'meta_short_description',
                  'order',
                  'prices',
                  'doctors',
                  'reviews',
                  'promotion',
                  'other_services'
                  ]
        
    def get_promotion(self, obj):
        promotions = Promotion.objects.filter(
            servicepromotion__service=obj
        )
        return PromotionSerializer(promotions, many=True).data
        
    def get_other_services(self, obj):
        services = Service.objects.filter(
            is_active=True
            ).exclude(
                id=obj.id
                ).order_by('order')[:4]

        return ServiceCardSerializer(
            services,many=True
            ).data