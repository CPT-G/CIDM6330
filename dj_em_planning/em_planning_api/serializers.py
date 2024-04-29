from rest_framework import serializers
from .models import User, EMData, LatLongPoints, Colors, FrequencyDevice, DataConversion, DateTime, FakePlotting, Mapping, Layout


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class EMDataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EMData
        fields = '__all__'


class LatLongPointsSerializer(serializers.ModelSerializer):
    class Meta:
        model = LatLongPoints
        fields = '__all__'


class ColorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Colors
        fields = '__all__'


class FrequencyDeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = FrequencyDevice
        fields = '__all__'


class DataConversionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataConversion
        fields = '__all__'


class DateTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DateTime
        fields = '__all__'


class FakePlottingSerializer(serializers.ModelSerializer):
    class Meta:
        model = FakePlotting
        fields = '__all__'


class MappingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mapping
        fields = '__all__'


class LayoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Layout
        fields = '__all__'
