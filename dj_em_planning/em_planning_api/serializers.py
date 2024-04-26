from rest_framework import serializers
# from em_planning.models import Item
# from django.contrib.auth.models import User
# from .models import LearningPath
# from .models import Bookmark, Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
# from django.contrib.auth.models import User
from em_planning_api.models import Customer

# class ItemSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Item
#         fields = '__all__'

# class LearningPathSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = LearningPath
#         fields = ("id", "title", "progress", "date")


# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ['url', 'username', 'email']

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'
