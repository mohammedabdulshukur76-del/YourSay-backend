from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_transactions, name='get_transactions'),
]