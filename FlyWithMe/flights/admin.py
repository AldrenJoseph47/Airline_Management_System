from django.contrib import admin
from .models import Flight


@admin.register(Flight)
class FlightAdmin(admin.ModelAdmin):
    list_display = ('flight_id', 'dep_airport', 'arr_airport', 'dep_date', 'arr_date')
    search_fields = ('flight_id',)
    list_filter = ('dep_airport', 'arr_airport')
