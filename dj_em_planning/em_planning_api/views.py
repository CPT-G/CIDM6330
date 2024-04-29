from rest_framework.response import Response
# from rest_framework.views import APIView
from .models import User, EMData, LatLongPoints, Colors, FrequencyDevice, DataConversion, DateTime, FakePlotting, Mapping, Layout
from django.shortcuts import render
from django.http import Http404
from rest_framework import status, permissions
from functools import wraps
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer, EMDataSerializer, LatLongPointsSerializer, ColorsSerializer
from .serializers import FrequencyDeviceSerializer, DataConversionSerializer, DateTimeSerializer
from .serializers import FakePlottingSerializer, MappingSerializer, LayoutSerializer
from rest_framework import viewsets
# Create your views here
# APIViews = GET, POST, PUT, DELETE


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class EMDataViewSet(viewsets.ModelViewSet):

    queryset = EMData.objects.all()
    serializer_class = EMDataSerializer


class LatLongPointsViewSet(viewsets.ModelViewSet):

    queryset = LatLongPoints.objects.all()
    serializer_class = LatLongPointsSerializer


class ColorsViewSet(viewsets.ModelViewSet):

    queryset = Colors.objects.all()
    serializer_class = ColorsSerializer


class FrequencyDeviceViewSet(viewsets.ModelViewSet):

    queryset = FrequencyDevice.objects.all()
    serializer_class = FrequencyDeviceSerializer


class DataConversionViewSet(viewsets.ModelViewSet):

    queryset = DataConversion.objects.all()
    serializer_class = DataConversionSerializer


class DateTimeViewSet(viewsets.ModelViewSet):

    queryset = DateTime.objects.all()
    serializer_class = DateTimeSerializer


class FakePlottingViewSet(viewsets.ModelViewSet):

    queryset = FakePlotting.objects.all()
    serializer_class = FakePlottingSerializer


class MappingViewSet(viewsets.ModelViewSet):

    queryset = Mapping.objects.all()
    serializer_class = MappingSerializer


class LayoutViewSet(viewsets.ModelViewSet):

    queryset = Layout.objects.all()
    serializer_class = LayoutSerializer

# class CustomerDetailView(APIView):
#     permission_classes = (IsAuthenticated,)

#     @resource_checker(Customer)
#     def get(self, request, pk, format=None):
#         customer = Customer.published.get(pk=pk)
#         serializer = CustomerSerializer(customer)
#         return Response(serializer.data)

#     @resource_checker(Customer)
#     def put(self, request, pk, format=None):
#         customer = Customer.published.get(pk=pk)
#         serializer = CustomerSerializer(customer, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     @resource_checker(Customer)
#     def delete(self, request, pk, format=None):
#         customer = Customer.published.get(pk=pk)
#         customer.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
