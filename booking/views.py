from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import (CreateView, UpdateView, DeleteView, FormView,
                                  TemplateView, ListView)
from .models import Booking, Table
from .forms import BookingForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin


class MakeBookingView(LoginRequiredMixin, CreateView):
    """ View to render booking form and allow user to make a reservation """

    form_class = BookingForm
    template_name = 'booking/booking.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # Check for available tables
            booking = form.save(commit=False)
            available_tables = Table.objects.filter(
                capacity__gte=booking.guests).exclude(
                booked_table__date=booking.date,
                booked_table__time=booking.time)
            if available_tables:
                # Assign a table to the booking
                booking.table_number = available_tables[0]
                booking.customer = request.user
                booking.save()
                return redirect('mybookings')
            else:
                form.add_error(None,
                               'No tables available for the selected date')
        return render(request, self.template_name, {'form': form})


class MyBookingsView(LoginRequiredMixin, ListView):
    """ View to display exsisting booking for customer """

    def get(self, request):
        customer = request.user
        if request.user.is_authenticated:
            bookings = (Booking.objects.filter(customer=self.request.user).
                        order_by('-date'))
            context = {
                    'customer': customer,
                    'bookings': bookings,
            }
            return render(request, 'booking/my_bookings.html', context)
        else:
            return render(request, 'account/login.html')


class DeleteBookingView(LoginRequiredMixin, DeleteView):
    """
    View to display delete booking page.
    """
    model = Booking
    template_name = 'booking/delete_booking.html'
    success_url = reverse_lazy('mybookings')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request,
                         'Your booking was deleted successfully.')
        return super(DeleteBookingView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return get_object_or_404(Booking, pk=self.kwargs.get("pk"),
                                 customer=self.request.user)
