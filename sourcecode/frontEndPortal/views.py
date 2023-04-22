from django.shortcuts import render
from django.views.generic import TemplateView,DetailView

# Create your views here.

class FrontEndPortal(TemplateView):
    template_name = 'frontEndPortal/index.html'
