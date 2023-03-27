from django.urls import path
from home.views import Homepage, MenuPage

urlpatterns = [
    path('', Homepage.as_view(), name='homepage'),
    path('menu/', MenuPage.as_view(), name='menu')
    ]
