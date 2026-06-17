from django.db import models


class Услуга(models.Model):
    meta_title = models.CharField(max_length=255, blank=True)
    meta_description = models.TextField(blank=True)
    slug = models.SlugField(unique=True)
    meta_short_description = models.TextField(blank=True)
    image = models.ImageField(upload_to='Услуги/')
    is_active = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"
        ordering = ['order']

    def __str__(self):
        return self.slug
    
class ЦенаУслуги(models.Model):
    service = models.ForeignKey(Услуга, on_delete=models.CASCADE, related_name='Цены')
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = "ЦенаУслуги"
        verbose_name_plural = "ЦенаУслуг"

class Продвижение(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='promotion/')

    class Meta:
        verbose_name = "Продвижение"
        verbose_name_plural = "Продвижения"

class СервисПродвижение(models.Model):
    service = models.ForeignKey(Услуга, on_delete=models.CASCADE, related_name='Продвижение')
    promotion = models.ForeignKey(Продвижение, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "СервисПродолжение"
        verbose_name_plural = "СервисПродолжения"

class Отзыв(models.Model):
    service = models.ForeignKey(Услуга, on_delete=models.CASCADE, related_name='отзывы')
    author = models.CharField(max_length=255)
    text = models.TextField()
    video = models.FileField(upload_to='отзывы/videos/', blank=True, null=True)
    photo = models.ImageField(upload_to='отзывы/photos/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author
    
    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"

class Врач(models.Model):
    service = models.ManyToManyField(Услуга, related_name='Врачи')
    full_name = models.CharField(max_length=255)
    specialty = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='Врачи/')
    description = models.TextField()

    def __str__(self):
        return self.full_name
    
    class Meta:
        verbose_name = "Врач"
        verbose_name_plural = "Врачи"

class СвязанныеУслуги(models.Model):
    service = models.ForeignKey(Услуга, on_delete=models.CASCADE, related_name='Связанные_услуги')
    related = models.ForeignKey(Услуга, on_delete=models.CASCADE, )

    class Meta:
        verbose_name = "СвязаннаяУслуга"
        verbose_name_plural = "СвязанныеУслуги"

class Контакты(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"