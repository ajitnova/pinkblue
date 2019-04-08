from django import forms
from .models import User, Inventory

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        feilds = "__all__"
        exclude = []

class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        feilds = "__all__"
        exclude = []