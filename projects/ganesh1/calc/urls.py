from django.urls import path
from . import views
from django.conf.urls import url
urlpatterns=[
    path('',views.home,name='home'),#homepage
    path('primes',views.primes,name='primes'),
    url(r'^calc/$', views.calc_list),
    url(r'^calc/(?P<pk>[0-9]+)/$', views.calc_detail),
    ]