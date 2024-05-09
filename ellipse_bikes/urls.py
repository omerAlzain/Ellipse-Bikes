from django.urls import path

from . import views


app_name = "ellipse_bikes"

urlpatterns = [
    path("", views.index, name="index"),
    path("contracts/", views.contracts, name="contracts"),
    path("<int:contract_id>/stations/", views.contract_stations, name="contract_stations"),
    path("stations/<int:station_id>", views.station_details, name="station_details"),

]