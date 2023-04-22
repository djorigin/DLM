from django.urls import path
from .views import FrontEndPortal




urlpatterns = [
    path('', FrontEndPortal.as_view(), name='frontEndPortal'),
]