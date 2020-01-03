from django.contrib import admin
from .models import Topping, Pizza_type,Topping_type, Pizza, Sub_addon, Sub, Pasta, Salad, Dinner_platter, Size, Cart_status, Cart, Order_status, Order

# Register your models here.
#class ToppingInline(admin.StackedInline):
    #model = Topping.pizzas.through
    #extra = 1

class PizzaAdmin(admin.ModelAdmin):
    filter_horizontal = ("topping",)

#class ToppingAdmin(admin.ModelAdmin):
    #filter_horizontal = ("pizzas",)

admin.site.register(Size)
admin.site.register(Pizza, PizzaAdmin)
admin.site.register(Pizza_type)
admin.site.register(Topping_type)
admin.site.register(Topping)
admin.site.register(Sub)
admin.site.register(Sub_addon)
admin.site.register(Pasta)
admin.site.register(Salad)
admin.site.register(Dinner_platter)
admin.site.register(Cart_status)
admin.site.register(Cart)
admin.site.register(Order_status)
admin.site.register(Order)
