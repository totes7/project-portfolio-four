from django.shortcuts import render
from django.views.generic import TemplateView


class Homepage(TemplateView):
    """ View to display homepage """
    template_name = 'home/index.html'
