from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/',          admin.site.urls),
    path('api/issues/',     include('issues.urls')),
    path('api/transactions/',    include('transactions.urls')),
    path('api/reviews/',        include('reviews.urls')),
    path('api/stats/',          views.get_stats, name='get_stats'),
]
