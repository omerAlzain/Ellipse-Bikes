import os
import datetime
import requests
from django.utils import timezone
from django.contrib.gis.geos import Point

from .. import models


get_stations_url = os.environ.get("GET_STATIONS_URL")+'?apiKey='+os.environ.get("API_KEY")
tz = timezone.get_current_timezone()


def update_stations():
    try:
        stations = requests.get(get_stations_url, headers={'Accept': 'application/json'}).json()
        for station in stations:
            contract = models.Contract.objects.filter(name=station['contractName']).first()
            station2 = models.Station.objects.filter(name=station['name']).first()
            if station2:

                station2.total_available_bikes = station['totalStands']['availabilities']['bikes']
                station2.total_available_stands = station['totalStands']['availabilities']['stands']
                station2.total_available_mechanical_bikes = station['totalStands']['availabilities']['mechanicalBikes']
                station2.total_available_electrical_bikes = station['totalStands']['availabilities']['electricalBikes']
                station2.total_available_electrical_internal_battery_bikes = station['totalStands']['availabilities'][
                    'electricalInternalBatteryBikes']
                station2.total_available_electrical_removable_battery_bikes = station['totalStands']['availabilities'][
                    'electricalRemovableBatteryBikes']
                station2.total_capacity = station['totalStands']['capacity']

                station2.main_available_bikes = station['mainStands']['availabilities']['bikes']
                station2.main_available_stands = station['mainStands']['availabilities']['stands']
                station2.main_available_mechanical_bikes = station['mainStands']['availabilities']['mechanicalBikes']
                station2.main_available_electrical_bikes = station['mainStands']['availabilities']['electricalBikes']
                station2.main_available_electrical_internal_battery_bikes = station['mainStands']['availabilities'][
                    'electricalInternalBatteryBikes']
                station2.main_available_electrical_removable_battery_bikes = station['mainStands']['availabilities'][
                    'electricalRemovableBatteryBikes']
                station2.main_capacity = station['mainStands']['capacity']
                if station['overflowStands']:
                    station2.overflow_available_bikes = station['overflowStands']['availabilities']['bikes']
                    station2.overflow_available_stands = station['overflowStands']['availabilities']['stands']
                    station2.overflow_available_mechanical_bikes = station['overflowStands']['availabilities'][
                        'mechanicalBikes']
                    station2.overflow_available_electrical_bikes = station['overflowStands']['availabilities'][
                        'electricalBikes']
                    station2.overflow_available_electrical_internal_battery_bikes = station['overflowStands']['availabilities'][
                        'electricalInternalBatteryBikes']
                    station2.overflow_available_electrical_removable_battery_bikes = station['overflowStands']['availabilities'][
                        'electricalRemovableBatteryBikes']
                    station2.overflow_capacity = station['overflowStands']['capacity']

                station2.status = station['status']
                station2.connected = station['connected']
                station2.last_update = datetime.datetime.strptime(station['lastUpdate'], '%Y-%m-%dT%H:%M:%SZ').astimezone(tz)

                station2.last_schedule_run = timezone.datetime.now(tz=tz)
                station2.save()
            else:
                if station['overflowStands']:
                    models.Station.objects.create(
                        # static data
                        number=station['number'],
                        contract=contract,
                        name=station['name'],
                        address=station['address'],
                        position=Point(station['position']['longitude'], station['position']['latitude']),

                        banking=station['banking'],
                        bonus=station['bonus'],
                        shape=station['shape'],
                        overflow=station['overflow'],
                        # dynamic data
                        status=station['status'],
                        connected=station['connected'],
                        # "2024-05-01T19:17:07Z"
                        last_update=datetime.datetime.strptime(station['lastUpdate'], '%Y-%m-%dT%H:%M:%SZ').astimezone(
                            tz),

                        total_available_bikes=station['totalStands']['availabilities']['bikes'],
                        total_available_stands=station['totalStands']['availabilities']['stands'],
                        total_available_mechanical_bikes=station['totalStands']['availabilities']['mechanicalBikes'],
                        total_available_electrical_bikes=station['totalStands']['availabilities']['electricalBikes'],
                        total_available_electrical_internal_battery_bikes=station['totalStands']['availabilities'][
                            'electricalInternalBatteryBikes'],
                        total_available_electrical_removable_battery_bikes=station['totalStands']['availabilities'][
                            'electricalRemovableBatteryBikes'],
                        total_capacity=station['totalStands']['capacity'],

                        main_available_bikes=station['mainStands']['availabilities']['bikes'],
                        main_available_stands=station['mainStands']['availabilities']['stands'],
                        main_available_mechanical_bikes=station['mainStands']['availabilities']['mechanicalBikes'],
                        main_available_electrical_bikes=station['mainStands']['availabilities']['electricalBikes'],
                        main_available_electrical_internal_battery_bikes=station['mainStands']['availabilities'][
                            'electricalInternalBatteryBikes'],
                        main_available_electrical_removable_battery_bikes=station['mainStands']['availabilities'][
                            'electricalRemovableBatteryBikes'],
                        main_capacity=station['mainStands']['capacity'],

                        overflow_available_bikes=station['overflowStands']['availabilities']['bikes'],
                        overflow_available_stands=station['overflowStands']['availabilities']['stands'],
                        overflow_available_mechanical_bikes=station['overflowStands']['availabilities'][
                            'mechanicalBikes'],
                        overflow_available_electrical_bikes=station['overflowStands']['availabilities'][
                            'electricalBikes'],
                        overflow_available_electrical_internal_battery_bikes=
                        station['overflowStands']['availabilities'][
                            'electricalInternalBatteryBikes'],
                        overflow_available_electrical_removable_battery_bikes=
                        station['overflowStands']['availabilities'][
                            'electricalRemovableBatteryBikes'],
                        overflow_capacity=station['overflowStands']['capacity'],

                        last_schedule_run=timezone.datetime.now(tz=tz)
                    )
                else:
                    models.Station.objects.create(
                        # static data
                        number=station['number'],
                        contract=contract,
                        name=station['name'],
                        address=station['address'],
                        position=Point(station['position']['longitude'], station['position']['latitude']),
                        banking=station['banking'],
                        bonus=station['bonus'],
                        shape=station['shape'],
                        overflow=station['overflow'],
                        # dynamic data
                        status=station['status'],
                        connected=station['connected'],
                        # "2024-05-01T19:17:07Z"
                        last_update=datetime.datetime.strptime(station['lastUpdate'], '%Y-%m-%dT%H:%M:%SZ').astimezone(
                            tz),

                        total_available_bikes=station['totalStands']['availabilities']['bikes'],
                        total_available_stands=station['totalStands']['availabilities']['stands'],
                        total_available_mechanical_bikes=station['totalStands']['availabilities']['mechanicalBikes'],
                        total_available_electrical_bikes=station['totalStands']['availabilities']['electricalBikes'],
                        total_available_electrical_internal_battery_bikes=station['totalStands']['availabilities'][
                            'electricalInternalBatteryBikes'],
                        total_available_electrical_removable_battery_bikes=station['totalStands']['availabilities'][
                            'electricalRemovableBatteryBikes'],
                        total_capacity=station['totalStands']['capacity'],

                        main_available_bikes=station['mainStands']['availabilities']['bikes'],
                        main_available_stands=station['mainStands']['availabilities']['stands'],
                        main_available_mechanical_bikes=station['mainStands']['availabilities']['mechanicalBikes'],
                        main_available_electrical_bikes=station['mainStands']['availabilities']['electricalBikes'],
                        main_available_electrical_internal_battery_bikes=station['mainStands']['availabilities'][
                            'electricalInternalBatteryBikes'],
                        main_available_electrical_removable_battery_bikes=station['mainStands']['availabilities'][
                            'electricalRemovableBatteryBikes'],
                        main_capacity=station['mainStands']['capacity'],

                        last_schedule_run=timezone.datetime.now(tz=tz)
                    )
    # except requests.exceptions.ConnectionError as e:
    #     print(e)
    # except requests.exceptions.Timeout as e:
    #     print(e)
    # except requests.exceptions.HTTPError as e:
    #     print(e)
    # except requests.exceptions.RequestException as e:
    #     print(e)
    except Exception as e:
        # TODO: Do some stuff here, like logging to a database table
        print(e)