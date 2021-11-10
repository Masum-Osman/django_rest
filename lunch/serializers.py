from django.db.models import fields
from rest_framework import serializers
from lunch.models import Restaurants, Menus, Employees, Votes

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model=Restaurants
        fields=('restaurantId', 'restaurantName', 'ownerName', 'createdOn')

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model=Menus
        fields=('menuId', 'restaurantId', 'title', 'type', 'summery', 'price', 'createdOn')


class EmployeesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employees
        fields=('employeeId', 'employeeName', 'department', 'dateOfJoining')

    
class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Votes
        fields=('voteId', 'employeeId', 'menuId', 'votedOn')