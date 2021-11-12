from django.conf.urls import url
from django.urls.resolvers import URLPattern
from lunch import views

urlpatterns=[
    url(r'^restaurant$', views.restaurantApi),
    url(r'^restaurant/([0-9]+)$', views.restaurantApi),

    url(r'^restaurant/menu$',views.menuApi),
    url(r'^restaurant/menu/([0-9]+)$',views.menuApi),

    url(r'^restaurant/menu/vote$',views.voteApi),
    url(r'^restaurant/menu/vote/([0-9]+)$',views.voteApi),

    url(r'^employee$',views.employeeApi),
    url(r'^employee/([0-9]+)$',views.employeeApi),
]