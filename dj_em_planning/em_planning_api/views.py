from rest_framework.response import Response
# from rest_framework.decorators import api_view
from rest_framework.views import APIView
# from em_planning_arch.models import Item
from em_planning_api.models import Customer
from em_planning_api.serializers import CustomerSerializer
from django.shortcuts import render
from django.http import Http404
from rest_framework import status, permissions
from functools import wraps
from rest_framework.permissions import IsAuthenticated
# from .serializers import ItemSerializer

# from django.contrib.auth.models import User
# from rest_framework import generics, permissions, renderers, viewsets
# from rest_framework.decorators import action

# from .models import Bookmark, Snippet
# from .permissions import IsOwnerOrReadOnly
# from .serializers import BookmarkSerializer, SnippetSerializer, UserSerializer

# Create your views here

# @api_view methods = GET, POST, PUT, DELETE


class CustomerView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        customers = Customer.published.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def resource_checker(model):
    def check_entity(fun):
        @wraps(fun)
        def inner_fun(*args, **kwargs):
            try:
                x = fun(*args, **kwargs)
                return x
            except model.DoesNotExist:
                return Response({'message': 'Not Found'}, status=status.HTTP_204_NO_CONTENT)
        return inner_fun
    return check_entity


class CustomerDetailView(APIView):
    permission_classes = (IsAuthenticated,)

    @resource_checker(Customer)
    def get(self, request, pk, format=None):
        customer = Customer.published.get(pk=pk)
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)

    @resource_checker(Customer)
    def put(self, request, pk, format=None):
        customer = Customer.published.get(pk=pk)
        serializer = CustomerSerializer(customer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @resource_checker(Customer)
    def delete(self, request, pk, format=None):
        customer = Customer.published.get(pk=pk)
        customer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
