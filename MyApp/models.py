from django.db import models
from .validators import validate_positive_or_zero

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[
                                validate_positive_or_zero])
    quantity = models.PositiveIntegerField(
        validators=[validate_positive_or_zero])

    def get_id_and_name(self):
        return f'{self.id} - {self.name}'

    def get_total_value(self):
        return self.price * self.quantity


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity_ordered = models.PositiveIntegerField(
        validators=[validate_positive_or_zero])

    def get_id_and_product_name(self):
        return f'{self.id} - {self.product.name}'

    def get_total_order_value(self):
        return self.product.price * self.quantity_ordered
