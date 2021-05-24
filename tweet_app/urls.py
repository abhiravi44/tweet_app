from django.urls import path
from .views import *

urlpatterns = [
    path('', signin,name='signin'),
    path('dashboard/',dashboard,name='dashboard'),
]
