from django.shortcuts import render
from django.views.generic import TemplateView


class Homepage(TemplateView):
    """ View to display homepage """
    template_name = 'home/index.html'


class MenuPage(TemplateView):
    """ View to display the menu page """
    template_name = 'home/menu.html'
