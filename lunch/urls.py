from django.conf.urls import url
from django.urls.resolvers import URLPattern
from lunch import views

urlpatterns=[
    url(r'^restaurant$', views.restaurantApi),
    url(r'^restaurant/([0-9]+)$', views.restaurantApi)
]

# URLPattern=[
#     url(r'^restaurant$', views.restaurantApi),
#     url(r'^restaurant/([0-9]+)$', views.restaurantApi)
# ]