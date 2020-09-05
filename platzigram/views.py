"""Platzigram views"""

# Django
from django.http import HttpResponse

# Utilidades
from datetime import datetime
import json #librería de json

def hello_world(request):
    """regresa un saludo"""
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse("Oh, hi! current server time is {now}".format(now=str(now)))

def sort_integers(request):
    """Regresa una respuesta JSON con enteros ordenados."""
    numbers = [int(i) for i in request.GET['numbers'].split(",")]
    sorted_ints = sorted(numbers)
    data = {
        'status': 'ok',
        'numbers': sorted_ints,
        'message': 'Integers sorted successfully.'
    }
    #import pdb; pdb.set_trace()
    #diccionario en formato json
    """
        json.dumps toma un diccionario y lo convierte a formato json        
    """
    return HttpResponse(
        json.dumps(data, indent=4),
         content_type='application/json'
    )

def say_hi(request,name, age):
    """ Regresa un saludo """
    if age<12:
        message = 'Sorry {}, you are not allowed here.'.format(name)
    else:
        message = 'Hello {}, Welcome to Platzigram'.format(name)
    
    return HttpResponse(message)