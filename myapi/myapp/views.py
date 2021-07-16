from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import GuitarSerializer

from myapp.models import Guitar

@api_view(['GET'])
def index(request):
    api_urls = {
        'List': '/guitar-list/',
        'Detail View': '/guitar-detail/<str:pk>/',
        'Create': '/guitar-create/',
        'Update': '/guitar-update/<str:pk>/',
        'Delete': '/guitar-delete/<str:pk>/',
    }
    return Response(api_urls)

@api_view(['GET'])
def guitar_list(request):
    guitars = Guitar.objects.all()
    serializer = GuitarSerializer(guitars, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def guitar_detail(request, pk):
    guitars = Guitar.objects.get(id=pk)
    serializer = GuitarSerializer(guitars, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def guitar_create(request):
    serializer = GuitarSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

