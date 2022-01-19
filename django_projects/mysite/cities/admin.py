from django.contrib import admin

from cities.models import City, State

# Register your models here.

admin.site.register(State)
admin.site.register(City)