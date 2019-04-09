from django.conf.urls import url, include
from django.contrib import admin
from inventory import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^admin/', admin.site.urls),
]
