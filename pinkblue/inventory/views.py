from rest_framework import generics
from django.shortcuts import render
from .forms import UserForm, InventoryForm
from .models import User, Inventory
from .serializers import UserSerializer, InventorySerializer

def inventory(self, request):
    queryset = Inventory.objects.all()
    if request.method == 'POST':
        form = InventoryForm(request.POST)
        if form.is_valid():
            form.save()
            form = InventoryForm()
    context = {'form' : form }
    inventory_data = {'queryset' : queryset}
    return render(request, 'inventory.html', inventory_data)

def index(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
    form = UserForm()
    context = {'form' : form }
    return render(request, 'index.html', context )

def create_user():
    return 0

def login():
    return 0

def store_assistant(request):
    return render(request, )

def store_manager(request):
    return render(request, )