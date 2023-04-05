from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import TemplateView, FormView
from .forms import ContactForm


class Homepage(TemplateView):
    """ View to display homepage """
    template_name = 'home/index.html'


class MenuPage(TemplateView):
    """ View to display the menu page """
    template_name = 'home/menu.html'


class ContactPage(FormView):
    """ View to display contact page """
    form_class = ContactForm
    template_name = 'home/contact.html'
    success_url = reverse_lazy('homepage')

    def contact(self, form):
        messages.add_message(request, messages.SUCCESS,
                             'Your message was sent successfully.')
        return super(ContactPage, self).contact(form)
