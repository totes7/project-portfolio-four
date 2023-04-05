from django.contrib import admin
from .models import Booking, Table


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    """ Admin options for booking model """
    fields = ('date', 'time', 'guests', 'table_number',
              'customer', 'name', 'email',
              'special_request', 'updated')
    list_display = ('name', 'email', 'date', 'time', 'guests', 'table_number',
                    'special_request')
    readonly_fields = ('date', 'time', 'guests', 'table_number',
                       'special_request')
    search_fields = ['name']
    list_filter = ('date', 'guests', 'updated')
    ordering = ('-date', '-time')
    # Allows admin to delete bookings
    actions = ['delete_selected']


@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    """ Admin options for table model """
    fields = ('id', 'number', 'capacity')
    list_display = ('id', 'number', 'capacity')
    readonly_fields = ['id']
    search_fields = ['capacity']
    list_filter = ('number', 'capacity')
    ordering = ['number']
    # Allows admin to delete tables
    actions = ['delete_selected']
