from rest_framework.response import Response
from rest_framework.decorators import api_view
from em_planning.models import Item
from .serializers import ItemSerializer

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


@api_view(['GET'])
def getData(request):
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def addItem(request):
    serializer = ItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

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
