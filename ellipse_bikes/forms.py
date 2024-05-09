
from django.contrib.gis import forms
# ModelForm, CharField, ModelChoiceField, OSMWidget, PointField
# from django.forms import ModelForm
from ellipse_bikes.models import Station


class StationForm(forms.ModelForm):

    # Static data
    number = forms.IntegerField(disabled=True)
    contract = forms.ModelChoiceField(queryset=Station.objects.all(), disabled=True)
    name = forms.CharField(max_length=200, disabled=True)
    address = forms.CharField(max_length=200, disabled=True)

    position = forms.PointField(widget=forms.OSMWidget(), disabled=True)
    shape = forms.CharField(max_length=200, disabled=True)
    overflow = forms.BooleanField(disabled=True)
    banking = forms.BooleanField(disabled=True)
    bonus = forms.BooleanField(disabled=True)

    # Dynamic data
    status = forms.CharField(max_length=8, disabled=True)
    last_update = forms.DateTimeField(disabled=True)

    connected = forms.BooleanField(disabled=True)

    total_available_bikes = forms.IntegerField(disabled=True)
    total_available_stands = forms.IntegerField(disabled=True)
    total_available_mechanical_bikes = forms.IntegerField(disabled=True)
    total_available_electrical_bikes = forms.IntegerField(disabled=True)
    total_available_electrical_internal_battery_bikes = forms.IntegerField(disabled=True)
    total_available_electrical_removable_battery_bikes = forms.IntegerField(disabled=True)
    total_capacity = forms.IntegerField(disabled=True)

    main_available_bikes = forms.IntegerField(disabled=True)
    main_available_stands = forms.IntegerField(disabled=True)
    main_available_mechanical_bikes = forms.IntegerField(disabled=True)
    main_available_electrical_bikes = forms.IntegerField(disabled=True)
    main_available_electrical_internal_battery_bikes = forms.IntegerField(disabled=True)
    main_available_electrical_removable_battery_bikes = forms.IntegerField(disabled=True)
    main_capacity = forms.IntegerField(disabled=True)

    overflow_available_bikes = forms.IntegerField(disabled=True)
    overflow_available_stands = forms.IntegerField(disabled=True)
    overflow_available_mechanical_bikes = forms.IntegerField(disabled=True)
    overflow_available_electrical_bikes = forms.IntegerField(disabled=True)
    overflow_available_electrical_internal_battery_bikes = forms.IntegerField(disabled=True)
    overflow_available_electrical_removable_battery_bikes = forms.IntegerField(disabled=True)
    overflow_capacity = forms.IntegerField(disabled=True)

    last_schedule_run = forms.DateTimeField(disabled=True)

    class Meta:
        model = Station
        fields = '__all__'
        # exclude = ['position']
        # widgets = {
        #     'position': OSMWidget(),
        # }
