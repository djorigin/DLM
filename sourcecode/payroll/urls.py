from django.urls import path
from .views import PayrollHome

urlpatterns = [
    path('home', PayrollHome.as_view(), name='payroll_home'),
]