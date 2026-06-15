from django.db import models


class Service(models.Model):
    meta_title = models.CharField(max_length=255, blank=True)
    meta_description = models.TextField(blank=True)
    slug = models.SlugField(unique=True)
    meta_short_description = models.TextField(blank=True)
    image = models.ImageField(upload_to='services/')
    is_active = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.slug
    
class ServicePrice(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='prices')
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)

class Promotion(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='promotion/')

class ServicePromotion(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='promotions')
    promotion = models.ForeignKey(Promotion, on_delete=models.CASCADE)

class Review(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='reviews')
    author = models.CharField(max_length=255)
    text = models.TextField()
    video = models.FileField(upload_to='reviews/videos/', blank=True, null=True)
    photo = models.ImageField(upload_to='reviews/photos/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author

class Doctor(models.Model):
    service = models.ManyToManyField(Service, related_name='doctors')
    full_name = models.CharField(max_length=255)
    specialty = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='doctors/')
    description = models.TextField()

    def __str__(self):
        return self.specialty

class RelatedService(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='related_services')
    related = models.ForeignKey(Service, on_delete=models.CASCADE)

class ContactRequest(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name