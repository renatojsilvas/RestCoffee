from django.urls import path, re_path

from coffeapi.level3 import views

urlpatterns = [  
    re_path(r'order(?:/(?P<id>\d+))?', views.dispatch, name='order'),
    path(r'payment/<int:id>', views.payment, name='payment'),
    path(r'receipt/<int:id>', views.receipt, name='receipt'),
]