from django.contrib import admin

# Register your models here.
from .models import Reservation, Menu, Type

admin.site.register(Reservation)
admin.site.register(Menu)
admin.site.register(Type)
