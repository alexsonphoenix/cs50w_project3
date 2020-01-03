from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Size(models.Model):
    """docstring for size."""
    size = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.size}"


class Pizza_type(models.Model):
    """docstring for Pizza_type."""
    Pizza_type_name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.Pizza_type_name}"


class Topping_type(models.Model):
    """docstring for Pizza_type."""
    Topping_type_name = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.Topping_type_name}"


class Topping(models.Model):
    """docstring for Topping."""
    topping_name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.topping_name}"


class Pizza(models.Model):
    """docstring for Pizza."""
    pizza_type = models.ForeignKey(Pizza_type, on_delete=models.CASCADE, related_name="pizza_kind")
    pizza_size = models.ForeignKey(Size, on_delete=models.CASCADE, related_name="pizza_size")
    topping_type = models.ForeignKey(Topping_type, on_delete=models.CASCADE, related_name="topping_kind")
    topping = models.ManyToManyField(Topping, blank=True, related_name="pizzas")
    price_small = models.FloatField()
    price_large = models.FloatField()

    def __str__(self):
        return f"{self.pizza_type} - {self.pizza_size} - {self.topping_type} - ({self.price_small}) - ({self.price_large})"



class Sub_addon(models.Model):
    """docstring for Sub_addon."""
    sub_addon_name = models.CharField(max_length=64)
    price = models.FloatField()

    def __str__(self):
        return f"{self.sub_addon_name} - ({self.price})"


class Sub(models.Model):
    """docstring for Subs."""
    sub_name = models.CharField(max_length=64)
    sub_size = models.ForeignKey(Size, on_delete=models.CASCADE, related_name="sub_size")
    sub_addon = models.ManyToManyField(Sub_addon, blank=True, related_name="sub_addons")
    price_small = models.FloatField()
    price_large = models.FloatField()

    def __str__(self):
        return f"{self.sub_name} - {self.sub_size} (With {self.sub_addon}) - ({self.price_small}) - ({self.price_large})"


class Pasta(models.Model):
    """docstring for Pasta."""
    pasta_name = models.CharField(max_length=64)
    price = models.FloatField()

    def __str__(self):
        return f"{self.pasta_name} - ({self.price})"


class Salad(models.Model):
    """docstring for Salad."""
    salad_name = models.CharField(max_length=64)
    price = models.FloatField()

    def __str__(self):
        return f"{self.salad_name} - ({self.price})"



class Dinner_platter(models.Model):
    """docstring for Salad."""
    plate_name = models.CharField(max_length=64)
    plate_size = models.ForeignKey(Size, on_delete=models.CASCADE, related_name="plate_size")
    price_small = models.FloatField()
    price_large = models.FloatField()

    def __str__(self):
        return f"{self.plate_name} - {self.plate_size} - ({self.price_small}) - ({self.price_large})"

class Cart_status(models.Model):
    """docstring for Cart status."""
    status = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.status}"


class Cart(models.Model):
    """docstring for Carts."""
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="client")
    pizzas = models.ManyToManyField(Pizza, blank=True, related_name="pizza_carts")
    subs = models.ManyToManyField(Sub, blank=True, related_name="sub_carts")
    pastas = models.ManyToManyField(Pasta, blank=True, related_name="pasta_carts")
    salads = models.ManyToManyField(Salad, blank=True, related_name="salad_carts")
    dinner_platters = models.ManyToManyField(Dinner_platter, blank=True, related_name="dinner_platter_carts")

    cart_status = models.ForeignKey(Cart_status, on_delete=models.CASCADE, related_name="cart_status")
    sum_price = models.FloatField()


    def __str__(self):
        return f"{self.customer} - ({self.sum_price}) - ({self.cart_status})"


class Order_status(models.Model):
    """docstring for Order status."""
    status = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.status}"

class Order(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE, related_name="customer")
    order_from_cart = models.ForeignKey(Cart, on_delete=models.CASCADE, blank=True, related_name="delivered_order")
    order_status = models.ForeignKey(Order_status, on_delete=models.CASCADE, related_name="order_status")

    def __str__(self):
        return f"{self.client} Order - {self.order_status} "
