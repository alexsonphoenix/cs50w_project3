from django.db import models

# Create your models here.
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


class Pizza(models.Model):
    """docstring for Pizza."""
    pizza_type = models.ForeignKey(Pizza_type, on_delete=models.CASCADE, related_name="pizza_kind")
    pizza_size = models.CharField(max_length=10)
    topping_type = models.ForeignKey(Topping_type, on_delete=models.CASCADE, related_name="topping_kind")
    price = models.FloatField()

    def __str__(self):
        return f"{self.pizza_type} - {self.pizza_size} - {self.topping_type} - ({self.price})"


class Topping(models.Model):
    """docstring for Topping."""
    topping_name = models.CharField(max_length=64)
    pizzas = models.ManyToManyField(Pizza, blank=True, related_name="toppings")

    def __str__(self):
        return f"{self.topping_name}"


class Sub_addon(models.Model):
    """docstring for Sub_addon."""
    sub_addon_name = models.CharField(max_length=64)
    price = models.FloatField()

    def __str__(self):
        return f"{self.topping_name} - ({self.price})"


class Sub(models.Model):
    """docstring for Subs."""
    sub_name = models.CharField(max_length=64)
    sub_size = models.CharField(max_length=10)
    sub_addon = models.ManyToManyField(Sub_addon, verbose_name="list of sub_addons")
    price = models.FloatField()

    def __str__(self):
        return f"{self.sub_name} - {self.sub_size} (With {self.sub_addon}) - ({self.price})"


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
    plate_size = models.CharField(max_length=10)
    price = models.FloatField()

    def __str__(self):
        return f"{self.plate_name} - {self.plate_size} - ({self.price})"
