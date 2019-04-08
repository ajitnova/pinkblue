from rest_framework import generics
from django.shortcuts import render
from .forms import UserForm, InventoryForm
from .models import User, Inventory
from .serializers import UserSerializer, InventorySerializer

def inventory(request):
    queryset = Inventory.objects.all()
    if request.method == 'POST':
        form = InventoryForm(request.POST)
        if form.is_valid():
            form.save()
            form = InventoryForm()
    form = InventoryForm()
    inventory_data = {'queryset' : queryset, 'form' : form}
    return render(request, 'inventory.html', inventory_data)

def index(request):
    if request.method == 'POST' and 'signin' in request.POST:
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
    if request.method == 'POST' and 'loginForm' in request.POST:
        username = request.POST['username']
        password = request.POST['password']
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