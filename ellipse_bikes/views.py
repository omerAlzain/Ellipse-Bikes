from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.gis import admin

from . import models
from . import forms


def index(request):
    context = {}
    return render(request, "ellipse_bikes/index.html", context)


def contracts(request):
    contract_list = models.Contract.objects.all()
    context = {'contract_list': contract_list, 'title': 'Contract List',
               'has_permission': True}
    return render(request, "ellipse_bikes/contracts.html", context)


def contract_stations(request, contract_id):
    contract = models.Contract.objects.get(pk=contract_id)
    contract_stations = contract.station_set.all().order_by('number')
    station_count = contract_stations.count()
    context = {'contract': contract, 'contract_stations': contract_stations,
               'station_count': station_count, 'title': 'Contract Stations'}
    return render(request, "ellipse_bikes/contract_stations.html", context)


def station_details(request, station_id):
    station = models.Station.objects.get(pk=station_id)
    form = forms.StationForm(instance=station)
    # media = form.media
    # admin_media = admin.ModelAdmin(models.City(), admin_site=admin.AdminSite()).media
    context = {'station': station, 'title': 'Station Data', 'form': form, }
    return render(request, 'ellipse_bikes/station_details.html', context)
