from django.contrib.auth import authenticate, login, logout

from django.db.utils import OperationalError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from orders.models import *
from django.contrib.auth.models import User


# Create your views here.
def index(request):
    context = {
        'pizzas_menu': list(Pizza.objects.all()),
        'toppings_menu': list(Topping.objects.all()),
        'subs_menu': list(Sub.objects.all()),
        'sub_addons_menu': list(Sub_addon.objects.all()),
        'pastas_menu': list(Pasta.objects.all()),
        'salads_menu': list(Salad.objects.all()),
        'dinner_platters_menu': list(Dinner_platter.objects.all()),
    }
    return render(request, "orders/index.html", context)



# Initialize scope varibles: (ONLY used for add_to_cart route)
try:
    cart_active_status = Cart_status.objects.get(status="active")
    cart_ordered_status = Cart_status.objects.get(status="ordered")
    cart_deleted_status = Cart_status.objects.get(status="deleted")
except OperationalError:
    pass  # happens when db doesn't exist yet, views.py should be
          # importable without this side effect
def add_to_cart(request, item_name, item_id):
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return render(request, "orders/login.html", {'message': "Please login to continue"})

        current_client = User.objects.get(username=request.user)
        # First, Check if there is any active cart
        try:
            currently_active_cart = Cart.objects.get(customer=current_client ,cart_status=cart_active_status)
        except Cart.DoesNotExist:
            currently_active_cart = Cart(customer=current_client, cart_status=cart_active_status, sum_price=0)
            currently_active_cart.save()
        except OperationalError:
            pass  # happens when db doesn't exist yet, views.py should be
                  # importable without this side effect

        print(currently_active_cart)

        # Classify different requests
        if item_name == "pizza":
            # create a clone of the chosen pizza to save
            copPizza = Pizza.objects.get(pk=item_id)
            newPizza = currently_active_cart.pizzas.add(copPizza)
            currently_active_cart.sum_price = float(currently_active_cart.sum_price) + float(copPizza.price_large)
            currently_active_cart.save()

            print("pizza added")

        elif item_name == "sub":
            # create a clone of the chosen item
            copSub = Sub.objects.get(pk=item_id)
            currently_active_cart.subs.add(copSub)
            currently_active_cart.sum_price =float(currently_active_cart.sum_price) + float(copSub.price_large)
            currently_active_cart.save()

            print("Sub added")

        elif item_name == "pasta":
            # create a clone of the chosen item
            copPasta = Pasta.objects.get(pk=item_id)
            currently_active_cart.pastas.add(copPasta)
            currently_active_cart.sum_price =float(currently_active_cart.sum_price) + float(copPasta.price)
            print("pasta added")

        elif item_name == "salad":
            # create a clone of the chosen item
            copSalad = Salad.objects.get(pk=item_id)
            currently_active_cart.salads.add(copSalad)
            currently_active_cart.sum_price =float(currently_active_cart.sum_price) + float(copSalad.price)
            currently_active_cart.save()

            print("salad added")

        elif item_name == "dinner_platter":
            # create a clone of the chosen item
            copDinner_platter = Dinner_platter.objects.get(pk=item_id)
            currently_active_cart.dinner_platters.add(copDinner_platter)
            currently_active_cart.sum_price =float(currently_active_cart.sum_price) + float(copDinner_platter.price_large)
            currently_active_cart.save()

            print("dish added")

        return JsonResponse({'item_added' : True})


#Initialize varibles for later uses
try:
    size_small = Size.objects.get(size="Small")
    size_large = Size.objects.get(size="Large")

    cheese_topping_type = Topping_type.objects.get(Topping_type_name="Cheese")
    one_topping_topping_type = Topping_type.objects.get(Topping_type_name="1 topping")
    two_topping_topping_type = Topping_type.objects.get(Topping_type_name="2 toppings")
    three_topping_topping_type = Topping_type.objects.get(Topping_type_name="3 toppings")
    special_topping_type = Topping_type.objects.get(Topping_type_name="Special")

except OperationalError:
    pass  # happens when db doesn't exist yet, views.py should be
          # importable without this side effect
def cart_view(request):
    if request.method == 'GET':
        if not request.user.is_authenticated:
            return render(request, "orders/login.html", {'message': "Please login to continue"})
        # Get the current client to further verification
        current_client = User.objects.get(username=request.user)
        # First, Check if there is any active cart
        try:
            currently_active_cart = Cart.objects.get(customer=current_client ,cart_status=cart_active_status)
        except Cart.DoesNotExist:
            currently_active_cart = Cart(customer=current_client, cart_status=cart_active_status, sum_price=0)
            currently_active_cart.save()
        except OperationalError:
            pass  # happens when db doesn't exist yet, views.py should be
                  # importable without this side effect

        context = {
            'currently_active_cart': currently_active_cart,

            'size_small': size_small,
            'size_large': size_large,

            'cheese_topping_type': cheese_topping_type,
            'one_topping_topping_type': one_topping_topping_type,
            'two_topping_topping_type': two_topping_topping_type,
            'three_topping_topping_type': three_topping_topping_type,
            'special_topping_type': special_topping_type,

            'steak_sub': Sub.objects.get(sub_name="Steak"),
            'extra_cheese_sub_addon': Sub_addon.objects.get(sub_addon_name='Extra Cheese on any sub'),
            'sub_addons_list': Sub_addon.objects.all(),

            'pizzas_in_cart' : currently_active_cart.pizzas.all(),
            'subs_in_cart' : currently_active_cart.subs.all(),
            'pastas_in_cart' : currently_active_cart.pastas.all(),
            'salads_in_cart' : currently_active_cart.salads.all(),
            'dinner_platters_in_cart' : currently_active_cart.dinner_platters.all(),

            'topping_types': Topping_type.objects.all(),
            'topping_list': Topping.objects.all(),
        }
        return render(request, "orders/cart.html", context)


def cart_change(request, decision, item_name, item_index):
    """Accept arguments: decision, item_name, item_index, """
    if request.method == "POST":
        # Ensure user is logged in
        if not request.user.is_authenticated:
            return render(request, "orders/login.html", {'message': "Please login to continue"})
        # Get the current client to further verification
        current_client = User.objects.get(username=request.user)
        # Get the currently active cart to start working on
        currently_active_cart = Cart.objects.get(customer=current_client ,cart_status=cart_active_status)

        print('decision is '+decision)

        if decision=="delete":
            # First, access the item:
            if item_name == "pizza":
                deletion = currently_active_cart.pizzas.all()
                deletion[item_index].delete()
                currently_active_cart.save()
                print("pizza with index: "+ str(item_index)+" is deleted")
            elif item_name == "sub":
                deletion = currently_active_cart.subs.all()
                deletion[item_index].delete()
                currently_active_cart.save()
                print("sub with index: "+ str(item_index)+" is deleted")
            elif item_name == "pasta":
                deletion = currently_active_cart.pastas.all()
                deletion[item_index].delete()
                currently_active_cart.save()
                print("pasta with index: "+ str(item_index)+" is deleted")
            elif item_name == "salad":
                deletion = currently_active_cart.salads.all()
                deletion[item_index].delete()
                currently_active_cart.save()
                print("salad with index: "+ str(item_index)+" is deleted")
            elif item_name == "dinner":
                deletion = currently_active_cart.dinner_platters.all()
                deletion[item_index].delete()
                currently_active_cart.save()
                print("dinner with index: "+ str(item_index)+" is deleted")

            return JsonResponse({'deleted': True})


# Store in the database (Orders table) the ordered items in Cart.
# def purchase():
#     if not request.user.is_authenticated:
#         return render(request, "orders/login.html", {'message': "Please login to continue"})
#     return JsonResponse({'value': True})


def login_view(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "orders/login.html", {"message": "Invalid credentials."})
    else:
        return render(request, "orders/login.html", {"message": None})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register_view(request):
    if request.method == 'POST':
        # Get Data from the Frontend
        username = request.POST["username"]
        password = request.POST["password"]
        email = request.POST["email"]
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]

        # Create New User
        new_user = User.objects.create_user(username, email, password)
        new_user.first_name = first_name
        new_user.last_name = last_name

        new_user.save()

        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "orders/register.html", {})

def check(request):
    try:
        username = request.POST["username"]
    except KeyError:
        raise "No username given"

    # length at least 1 and does not already belong to a user in the database
    if len(username) > 1 and User.objects.filter(username=username).count() == 0:
        return JsonResponse({'validity': True})
    else:
        return JsonResponse({'validity': False})
