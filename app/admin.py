from django.contrib import admin
from .models import *

admin.site.register(Service)
admin.site.register(ServicePrice)
admin.site.register(ServicePromotion)
admin.site.register(Promotion)
admin.site.register(Doctor)
admin.site.register(Review)
admin.site.register(RelatedService)
admin.site.register(ContactRequest)