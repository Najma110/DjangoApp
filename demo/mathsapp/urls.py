from django.urls import path
from . import views

from django.urls import path
from . import views

urlpatterns = [
    path('', views.calculate, name='home'),
    # Include other URL patterns as needed
]