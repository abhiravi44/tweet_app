from django.urls import path
from .views import *

urlpatterns = [
    path('', signin,name='signin'),
    path('dashboard/',dashboard,name='dashboard'),
    path('follow/<int:id>/',follow,name='follow'),
    path('profile/<int:id>/',profile,name='profile'),
    path('all/',all_users,name='all_users'),
]
