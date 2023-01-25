from django.db import models


class Products(models.Model):
    name = models.CharField(max_length=64)
    descriptions = models.TextField(blank=True, null=True, default=None)

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Добавлено")  # date created
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Изменено")  # date update

    class Meta:
        verbose_name_plural = 'Товар'
        verbose_name = 'Товары'

    def __str__(self):
        return '%s' % self.name


class ProductImage(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE, blank=True, null=True, default=None)
    image = models.ImageField(upload_to='product_images/')
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Добавлено")  # date created
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Изменено")  # date update

    class Meta:
        verbose_name_plural = 'Фотографии'
        verbose_name = 'Фотографии продукта'

    def __str__(self):
        return str(self.id)