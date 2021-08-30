from ..models import Measurement

def get_all_measurements():
    measurements = Measurement.objects.all()
    return measurements


def get_measurement_by_pk(num):
    measurement = Measurement.objects.filter(pk=num)
    return measurement

def delete_measurement_by_pk(num):
    measurement = Measurement.objects.filter(pk=num).delete()
    measurementsNow = Measurement.objects.all()
    return measurementsNow

def update_measurement_by_pk(num, val):
    measurement = Measurement.objects.get(pk=num)
    measurement.value = val
    measurement.save()

    measurements = Measurement.objects.all()
    return measurements