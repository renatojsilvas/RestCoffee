from django.urls import include, path

urlpatterns = [   
    path('', include('coffeapi.level0.urls')),    
    path('', include('coffeapi.level1.urls')),
    path('', include('coffeapi.level2.urls')),    
    path('', include('coffeapi.level3.urls')),    
]