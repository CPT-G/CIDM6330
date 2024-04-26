from rest_framework.response import Response
# from rest_framework.decorators import api_view
from rest_framework.views import APIView
# from em_planning_arch.models import Item
from em_planning_api.models import Customer
from em_planning_api.serializers import CustomerSerializer
from django.shortcuts import render
from rest_framework import status
from functools import wraps
# from .serializers import ItemSerializer

# from django.shortcuts import render
# from django.contrib.auth.models import User
# from rest_framework import generics, permissions, renderers, viewsets
# from rest_framework.decorators import action

# from .models import Bookmark, Snippet
# from .permissions import IsOwnerOrReadOnly
# from .serializers import BookmarkSerializer, SnippetSerializer, UserSerializer

# from .models import LearningPath
# from api.serializers import UserSerializer, LearningPathSerializer

# Create your views here

# @api_view methods = GET, POST, PUT, DELETE


class CustomerView(APIView):
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


class CustomerDetailView(APIView):
    """
    docstring
    """


def resource_checker(model):

    def check_entity(fun):
        @wraps(fun)
        def inner_fun(*args, **kwargs):
            try:
                x = fun(*args, **kwargs)
                return x
            except model.DoesNotExist:
                return Response({'messg': 'Not Found'}, status=status.HTTP_204_NO_CONTENT)
            return inner_fun
        return check_entity

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

        # @api_view(['GET'])
        # def getData(request):
        #     items = Item.objects.all()
        #     serializer = ItemSerializer(items, many=True)
        #     return Response(serializer.data)

        # @api_view(['POST'])
        # def addItem(request):
        #     serializer = ItemSerializer(data=request.data)
        #     if serializer.is_valid():
        #         serializer.save()
        #     return Response(serializer.data)

        # class UserViewSet(viewsets.ModelViewSet):
        #     """
        #     API endpoint that allows users to be viewed or edited.
        #     """
        #     queryset = User.objects.all().order_by('-date_joined')
        #     serializer_class = UserSerializer
        #     permission_classes = [permissions.IsAuthenticated]

        # class LearningPathViewSet(viewsets.ModelViewSet):
        #     """
        #     API endpoint that allows learning paths to be viewed or edited.
        #     """
        #     queryset = LearningPath.objects.all().order_by("date")
        #     serializer_class = LearningPathSerializer
