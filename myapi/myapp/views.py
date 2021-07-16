from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

import json

from myapp.models import Guitar

def index(request):
    response = json.dumps([{}])
    return HttpResponse(response, content_type='text/json')

def get_guitar(request, guitar_name):
    if request.method == 'GET':
        try:
            guitar = Guitar.objects.get(name=guitar_name)
            response = json.dumps([{ 'Guitar': guitar.name, 'Price': guitar.price}])
        except:
            response = json.dumps([{ 'Error': 'No guitar with that name'}])
    return HttpResponse(response, content_type='text/json')