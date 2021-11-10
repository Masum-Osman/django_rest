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
    elif request.method == 'POST':
        restaurant_data = JSONParser().parse(request)
        restaurant_serializer = RestaurantSerializer(data=restaurant_data)
        if restaurant_serializer.is_valid():
            restaurant_serializer.save()
            return JsonResponse("restaurant added successfully", safe=False)
        return JsonResponse("failed to add new restaurant", safe=False)