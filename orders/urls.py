from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("login", views.login_view, name='login'),
    path("logout", views.logout_view, name='logout'),
    path("register", views.register_view, name='register'),
    path("check", views.check, name='check'),
    path("cart", views.cart_view, name='cart'),
    path("cart_change/<str:decision>/<str:item_name>/<int:item_index>", views.cart_change, name='cart_change'),
    path("add_to_cart/<str:item_name>/<int:item_id>", views.add_to_cart, name='add_to_cart'),
    # path("purchase", views.purchase, name='purchase')
]
