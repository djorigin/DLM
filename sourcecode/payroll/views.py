from django.shortcuts import render
from django.views.generic import TemplateView,DetailView

# Create your views here.

class PayrollHome(TemplateView):
    template_name = 'payroll/payroll_home.html'
    