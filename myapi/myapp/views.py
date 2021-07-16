from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

# from django.views.decorators.csrf import csrf_exempt

import json

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

# def guitar_list(request):
#     if request.method == 'GET':
#         try:
#             guitars = Guitar.objects.all()
#             guitar_list = list(guitars)
#             response = json.dumps(guitar_list)
#         except:
#             response = json.dumps([{ 'Error': 'No guitars found'}])
#     return HttpResponse(response, content_type='text/json')


# def get_guitar(request, guitar_name):
#     if request.method == 'GET':
#         try:
#             guitar = Guitar.objects.get(name=guitar_name)
#             response = json.dumps([{ 'Guitar': guitar.name, 'Price': guitar.price}])
#         except:
#             response = json.dumps([{ 'Error': 'No guitar with that name'}])
#     return HttpResponse(response, content_type='text/json')