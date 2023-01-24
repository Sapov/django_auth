from django.db import models


class Order(models.Model):
    customer_name = models.CharField(max_length=20)
    customer_email = models.EmailField()
    customer_phone = models.CharField(max_length=20, blank=True, null=True, default=None)
    comments = models.TextField(blank=True, null=True, default=None)

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Добавлено")  # date created
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Изменено")  # date update

    class Meta:
        verbose_name_plural = 'Заказ'
        verbose_name = 'Заказы'

    def __str__(self):
        return str(self.id)


class ProductInOrder(models.Model):
    order = models.ForeignKey(Order, blank=True, null=True, default=None)
    product = models.ForeignKey(Product, blank=True, null=True, default=None)
    customer_name = models.CharField(max_length=20)
    customer_email = models.EmailField()
    customer_phone = models.CharField(max_length=20, blank=True, null=True, default=None)

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Добавлено")  # date created
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Изменено")  # date update

    class Meta:
        verbose_name_plural = 'Заказ'
        verbose_name = 'Заказы'

    def __str__(self):
        return str(self.id)
