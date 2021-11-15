import logging
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from lunch.models import Restaurants, Employees, Menus, Votes
from lunch.serializers import RestaurantSerializer, EmployeesSerializer, MenuSerializer, VoteSerializer
from _datetime import date

# Create your views here.

@csrf_exempt
def restaurantApi(request, id=0):
    if request.method == 'GET':
        logging.info()
        restaurant = Restaurants.objects.all()
        restaurant_serializer = RestaurantSerializer(restaurant, many=True)
        return JsonResponse(restaurant_serializer.data, safe=False)
    elif request.method == 'POST':
        restaurant_data = JSONParser().parse(request)
        restaurant_serializer = RestaurantSerializer(data=restaurant_data)
        if restaurant_serializer.is_valid():
            restaurant_serializer.save()
            return JsonResponse("added successfully", safe=False)
        return JsonResponse("failed to add", safe=False)

    elif request.method=='GET':
        restaurant_data=JSONParser().parse(request)
        restaurant=Restaurants.objects.get(restaurantId=restaurant_data['restaurantId'])
        restaurant_serializer = RestaurantSerializer(restaurant, many=False)
        return JsonResponse(restaurant_serializer.data, safe=False)


@csrf_exempt
def menuApi(request, id=0):
    if request.method == 'GET':
        menus = Menus.objects.filter(createdOn=date.today())
        menu_serializer = MenuSerializer(menus, many=True)
        return JsonResponse(menu_serializer.data, safe=False)
    elif request.method == 'POST':
        menu_data = JSONParser().parse(request)
        menu_serializer = MenuSerializer(data=menu_data)
        if menu_serializer.is_valid():
            menu_serializer.save()
            return JsonResponse("menu added successfully", safe=False)
        return JsonResponse("menu added failed", safe=False)


@csrf_exempt
def employeeApi(request, id=0):
    if request.method == 'GET':
        emp = Employees.objects.all()
        emp_serializer = EmployeesSerializer(emp, many=True)
        return JsonResponse(emp_serializer.data, safe=False)
    elif request.method == 'POST':
        emp_data = JSONParser().parse(request)
        emp_serializer = EmployeesSerializer(data=emp_data)
        if emp_serializer.is_valid():
            emp_serializer.save()
            return JsonResponse("employee added successfully", safe=False)
        return JsonResponse("employee added failed", safe=False)


@csrf_exempt
def voteApi(request, id=0):
    if request.method == 'GET':
        vote = Votes.objects.filter(votedOn=date.today())
        vote_serializer = VoteSerializer(vote, many=True)
        return JsonResponse(vote_serializer.data, safe=False)
    elif request.method == 'POST':
        vote_data = JSONParser().parse(request)
        vote_serializer = VoteSerializer(data=vote_data)
        if vote_serializer.is_valid():
            vote_serializer.save()
            return JsonResponse("vote added successfully", safe=False)
        return JsonResponse("vote added failed", safe=False)
    elif request.method == 'PUT':
        vote_data = JSONParser().parse(request)
        vote_serializer = VoteSerializer(data=vote_data)
        if vote_serializer.is_valid():
            vote_serializer.save()
            return JsonResponse("vote added successfully", safe=False)
        return JsonResponse("vote added failed", safe=False)
