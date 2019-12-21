from django.contrib import admin
from .models import Topping, Pizza_type,Topping_type, Pizza, Sub_addon, Sub, Pasta, Salad, Dinner_platter

# Register your models here.
class ToppingInline(admin.StackedInline):
    model = Topping.pizzas.through
    extra = 1

class PizzaAdmin(admin.ModelAdmin):
    inlines = [ToppingInline]

class ToppingAdmin(admin.ModelAdmin):
    filter_horizontal = ("pizzas",)

admin.site.register(Pizza, PizzaAdmin)
admin.site.register(Pizza_type)
admin.site.register(Topping_type)
admin.site.register(Topping, ToppingAdmin)
admin.site.register(Sub)
admin.site.register(Sub_addon)
admin.site.register(Pasta)
admin.site.register(Salad)
admin.site.register(Dinner_platter)
