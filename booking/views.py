from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import (CreateView, UpdateView, DeleteView, FormView,
                                  TemplateView)
from .models import Booking
from .forms import BookingForm
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
            new_form = form.save(commit=False)
            new_form.user = request.user
            new_form.save()
        return render(request, self.template_name, {'form': form})
