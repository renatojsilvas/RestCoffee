from django.urls import path

from coffeapi.level0.views import barista

urlpatterns = [
    path('PlaceOrder', barista),        
]