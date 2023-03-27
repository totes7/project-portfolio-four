from django.urls import path
from . import views

urlpatterns = [
    path('makebooking/', views.MakeBookingView.as_view(), name='makebooking')
]
