from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('/assistant', views.store_assistant, name="store_assistant"),
    path('/manager', views.store_manager, name="store_manager"),
    path('/inventory', views.inventory, name="inventory")
]