from django.urls import path,include
from rest_framework import routers
from . import views
from django.conf.urls import url


router=routers.DefaultRouter()
router.register(r'apibase',views.APIBASEViewSet)

urlpatterns=[
    path('',views.home,name='home'),#homepage
    path('primes',views.primes,name='primes'),
    #url(r'^calc/$', views.calc_list),
    #url(r'^calc/(?P<pk>[0-9]+)/$', views.calc_detail),
    #path('admin/', admin.site.urls),
    path('', include(router.urls)),
    #path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    ]