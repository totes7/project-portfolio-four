from django.urls import path
from . import views

urlpatterns = [
    path('makebooking/', views.MakeBookingView.as_view(), name='makebooking'),
    path('mybookings/', views.MyBookingsView.as_view(), name='mybookings'),
    path('mybookings/edit_booking/<int:pk>',
         views.EditBookingView.as_view(),
         name='edit_booking'),
    path('mybookings/<int:pk>/delete_booking',
         views.DeleteBookingView.as_view(),
         name='delete_booking')
]
