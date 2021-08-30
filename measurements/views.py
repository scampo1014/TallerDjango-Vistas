from django.shortcuts import render
from .logic.logic_measurements import get_all_measurements, get_measurement_by_pk, delete_measurement_by_pk, update_measurement_by_pk
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def get_measurements(request):
    measurements = get_all_measurements()
    measurement_list = serializers.serialize('json', measurements)
    return HttpResponse(measurement_list, content_type='application/json')

def get_measurement(request, pk):
    measurement = get_measurement_by_pk(pk)
    measurement_list = serializers.serialize('json', measurement)
    return HttpResponse(measurement_list, content_type='application/json')

def delete_measurement(request, pk):
    measurementsAfter = delete_measurement_by_pk(pk)
    measurement_list = serializers.serialize('json', measurementsAfter)
    return HttpResponse(measurement_list, content_type='application/json')

def update_measurement(request, pk, val):
    measurement = update_measurement_by_pk(pk, val)
    measurement_list = serializers.serialize('json', measurement)
    return HttpResponse(measurement_list, content_type='application/json')