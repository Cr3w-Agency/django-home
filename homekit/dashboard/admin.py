from django.contrib import admin
from .models import *
# Register your models here.

class TemperatureAdmin(admin.ModelAdmin):
    list_display = ('value', 'created_at', 'room')

    class Meta:
        model = Temperature
        fields = '__all__'
        list_filter = ('-created_at',)

class HumidityAdmin(admin.ModelAdmin):
    list_display = ('value', 'created_at', 'room')

    class Meta:
        model = Temperature
        fields = '__all__'
        list_filter = ('created_at',)

class PressureAdmin(admin.ModelAdmin):
    list_display = ('value', 'created_at', 'room')

    class Meta:
        model = Temperature
        fields = '__all__'
        list_filter = ('created_at',)


admin.site.register(Temperature, TemperatureAdmin)
admin.site.register(Humidity, HumidityAdmin)
admin.site.register(Pressure, PressureAdmin)
admin.site.register(Place)