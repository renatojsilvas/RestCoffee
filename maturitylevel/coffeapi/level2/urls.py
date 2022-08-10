from django.urls import path, re_path

from coffeapi.level2 import views

urlpatterns = [  
    re_path(r'order_old(?:/(?P<id>\d+))?', views.dispatch, name='order_old'),
]