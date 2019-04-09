from rest_framework import generics
from django.shortcuts import render
from .forms import UserForm, InventoryForm, LoginForm
from .models import User, Inventory
from .serializers import UserSerializer, InventorySerializer

def index(request):
    if request.method == 'POST':
        if 'signup' in request.POST:
            form = UserForm(request.POST)
            if form.is_valid():
                form.save()
                
        if 'login' in request.POST:
            form = LoginForm(request.POST)
            username = form['username'].value()
            password = form['password'].value()
            user = User.objects.filter(user_name = username)
            for value in user:
                if username == value.user_name and password == value.password:
                        queryset = Inventory.objects.all()
                        if request.method == 'POST':
                            form = InventoryForm(request.POST)
                            if form.is_valid():
                                form.save()
                        if value.role == "A":
                            form = "Manager Approval to edit Database"
                        elif value.role == "M":
                            form = InventoryForm()
                        inventory_data = {'queryset' : queryset, 'form' : form}
                        return render(request, 'inventory.html', inventory_data)

        if 'product' in request.POST:
            queryset = Inventory.objects.all()
            form = InventoryForm(request.POST)
            if form.is_valid():
                form.save()
            if value.role == "A":
                form = "Manager Approval to edit Database"
            elif value.role == "M":
                form = InventoryForm()
            inventory_data = {'queryset' : queryset, 'form' : form}
            return render(request, 'inventory.html', inventory_data)

    sign_up = UserForm()
    login = LoginForm()
    context = {'sign_up' : sign_up, 'login' : login }
    return render(request, 'index.html', context )