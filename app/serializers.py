from rest_framework import serializers
from .models import Услуга, СервисПродвижение, СвязанныеУслуги,ЦенаУслуги, Продвижение,Отзыв, Врач, Контакты

class ServicePriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ЦенаУслуги
        fields = ['id','name', 'price']

class PromotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Продвижение
        fields = ['id','title','description','image']

class ServiceCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Услуга
        fields = ['id','meta_title','slug','image']

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Отзыв
        fields = ['id',
                  'author',
                  'text',
                  'video',
                  'photo',
                  'created_at'
                  ]

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Врач
        fields = ['id',
                  'full_name',
                  'specialty',
                  'photo',
                  'description'
                  ]
        
class ContactRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Контакты
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
        model = Услуга
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
        promotions = Продвижение.objects.filter(
            servicepromotion__service=obj
        )
        return PromotionSerializer(promotions, many=True).data
        
    def get_other_services(self, obj):
        services = Услуга.objects.filter(
            is_active=True
            ).exclude(
                id=obj.id
                ).order_by('order')[:4]

        return ServiceCardSerializer(
            services,many=True
            ).data