from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from lunch.models import Restaurants, Employees, Menus, Votes
from lunch.serializers import RestaurantSerializer, EmployeesSerializer, MenuSerializer, VoteSerializer

# Create your views here.

@csrf_exempt
def restaurantApi(request, id=0):
    if request.method == 'GET':
        restaurant = Restaurants.objects.all()
        restaurant_serializer = RestaurantSerializer(restaurant, many=True)
        return JsonResponse(restaurant_serializer.data, safe=False)