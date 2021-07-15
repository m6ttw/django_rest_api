from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

import json

def index(request):
    response = json.dumps([{}])
    return HttpResponse(response, content_type='text/json')
