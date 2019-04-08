from django.db import models
from datetime import date

class User(models.Model):
    ROLE_CHOICES = (
        ("A","Store Assistant"),
        ("M", "Store Manager")
    )
    user_name = models.CharField(max_length=100, primary_key=True, blank=False)
    password = models.CharField(max_length=100, blank=False)
    email = models.EmailField(max_length=70, blank=False)
    role = models.CharField(max_length=100, choices = ROLE_CHOICES)

class Inventory(models.Model):
    STATUS_CHOICES = (
        ("A","Approved"),
        ("P", "Pending")
    )
    product_id = models.CharField(max_length=100, blank=False)
    product_name = models.CharField(max_length=100, blank=False)
    vendor = models.CharField(max_length=100, blank=False)
    mrp = models.FloatField()
    batch_num = models.PositiveIntegerField()
    batch_date = models.DateField(default=date.today)
    quantity = models.PositiveIntegerField()
    status = models.CharField(max_length = 1, choices = STATUS_CHOICES)