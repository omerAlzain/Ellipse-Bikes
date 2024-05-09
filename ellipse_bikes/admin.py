from django.contrib.gis import admin
from . import models
# Register your models here.


class CityAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


class ContractAdmin(admin.ModelAdmin):
    list_display = ('name', 'commercial_name', 'country_code', 'display_cities')
    search_fields = ('name', 'commercial_name', 'country_code',)


class GISStationAdmin(admin.GISModelAdmin):
    fieldsets = [('Static Fields', {'fields': ('number', 'contract', 'name', 'address', 'shape',
                                               'overflow', 'banking', 'bonus')}),
                 ('GIS Fields', {'fields': ('position',)}),
                 ('Dynamic Fields', {'fields': ('connected',
                                                'status', 'last_update', 'last_schedule_run')}),
                 ('Total Availabilities', {'fields': ('total_available_bikes',
                                                      'total_available_stands',
                                                      'total_available_mechanical_bikes',
                                                      'total_available_electrical_bikes',
                                                      'total_available_electrical_internal_battery_bikes',
                                                      'total_available_electrical_removable_battery_bikes',
                                                      'total_capacity')}),
                 ('Main Availabilities', {'fields':  ('main_available_bikes',
                                                      'main_available_stands',
                                                      'main_available_mechanical_bikes',
                                                      'main_available_electrical_bikes',
                                                      'main_available_electrical_internal_battery_bikes',
                                                      'main_available_electrical_removable_battery_bikes',
                                                      'main_capacity')}),
                 ('Overflow Availabilities', {'fields': (
                                                        'overflow_available_bikes',
                                                        'overflow_available_stands',
                                                        'overflow_available_mechanical_bikes',
                                                        'overflow_available_electrical_bikes',
                                                        'overflow_available_electrical_internal_battery_bikes',
                                                        'overflow_available_electrical_removable_battery_bikes',
                                                        'overflow_capacity')}),
                 ]
    list_display = ('number', 'contract_name','name', 'connected', 'status')
    search_fields = ('name', 'status')
    list_filter = ('contract',)


admin.site.register(models.City, CityAdmin)
admin.site.register(models.Contract, ContractAdmin)
admin.site.register(models.Station, GISStationAdmin)
