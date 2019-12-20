from django.contrib import admin
from .models import Topping, Pizza_type, Pizza, Sub_addon, Sub, Pasta, Salad, Dinner_platter

# Register your models here.
admin.site.register(Pizza)
admin.site.register(Pizza_type)
admin.site.register(Topping)
admin.site.register(Sub)
admin.site.register(Sub_addon)
admin.site.register(Pasta)
admin.site.register(Salad)
admin.site.register(Dinner_platter)
