from django.http import request
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .models import Car
from .forms import CreateUserForm
# Create your views here.


def home_view(request):
    return render(request, "cars/home.html")


def about_view(request):
    return render(request, "cars/about.html")


def contact_view(request):
    return render(request, "cars/contact.html")


def login_view(request):

    if request.method == 'POST':
        username = request.POST.get('user_name')
        password = request.POST.get('user_password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username OR Password is incorrect')
    context = {}
    return render(request, "cars/login.html", context)


def logout_user(request):
    logout(request)
    return redirect('login')


def UserDetailView(request):

    return render(request, "cars/user.html")


def register_view(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('login')

    context = {
        'form': form
    }
    return render(request, "cars/register.html", context)


class CarListView(ListView):
    model = Car
    template_name = "cars/cars.html"


class CarDetailView(DetailView):
    model = Car
    template_name = "cars/cardetail.html"
