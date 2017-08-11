from django.contrib import admin

# Register your models here.
from entities.models import User, Service, Appointment

admin.site.register(User)
admin.site.register(Service)
admin.site.register(Appointment)