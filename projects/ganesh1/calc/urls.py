from django.urls import path
from . import views
urlpatterns=[
    path('',views.home,name='home'),#homepage
    path('primes',views.primes,name='primes'),
    ]