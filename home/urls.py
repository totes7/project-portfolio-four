from django.urls import path
from home.views import Homepage, MenuPage, ContactPage

urlpatterns = [
    path('', Homepage.as_view(), name='homepage'),
    path('menu/', MenuPage.as_view(), name='menu'),
    path('contact/', ContactPage.as_view(), name='contact')
    ]
