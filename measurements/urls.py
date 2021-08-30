from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.get_measurements, name='measurementList'),
    path('<int:pk>', views.get_measurement, name='measurement'),
    path('del/<int:pk>', views.delete_measurement, name='del_measurement'),
    path('update/<int:pk>-<int:val>', views.update_measurement, name='update-measurement')
]