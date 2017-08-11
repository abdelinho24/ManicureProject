from entities.models import User, Service, Appointment
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('firstname', 'lastname', 'phone_number', 'type', 'date_of_birth', 'sex', 'address', 'rate', 'email')


class ServiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Service
        fields = ('name', 'category', 'duration', 'price')


class AppointmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Appointment
        fields = ('name', 'date', 'pro', 'customer')