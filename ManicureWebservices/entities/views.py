from django.shortcuts import render


from rest_framework import viewsets
from rest_framework import permissions
from entities.models import User, Service, Appointment
from entities.serializers import UserSerializer, AppointmentSerializer, ServiceSerializer


# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer