from django.contrib.auth import authenticate, login, logout

from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse

from orders.models import *
from django.contrib.auth.models import User


# Create your views here.
def index(request):

    return render(request, "orders/index.html", {})


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
