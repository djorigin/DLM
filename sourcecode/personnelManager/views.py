from django.shortcuts import render
from django.views.generic import TemplateView,DetailView

# Create your views here.

class IndexView(TemplateView):
    template_name = 'personnelManager/home.html'
