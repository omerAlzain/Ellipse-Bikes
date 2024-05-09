import json
import datetime
from pathlib import Path

from django.contrib.gis.geos import Point
from django.db import migrations
from django.utils import timezone


# More into how to migrate data:
# https://docs.djangoproject.com/en/5.0/topics/migrations/#data-migrations
tz = timezone.get_current_timezone()
data_file_path = Path(__file__).parent.parent.resolve() / 'data' / 'stations_v3.json'
with open(data_file_path, 'r', encoding='utf8') as f:
    stations = json.load(f)


def insert_station(apps, schema_editor):
    # We can't import the Station model directly as it may be a newer
    # version than this migration expects. We use the historical version.
    Station = apps.get_model("ellipse_bikes", "Station")
    Contract = apps.get_model("ellipse_bikes", "Contract")
    for station in stations:
        contract = Contract.objects.filter(name=station['contractName']).first()
        if not contract:
            Contract.objects.create(name=station['contractName'])
        # get complains if there is no object with the name
        station2 = Station.objects.filter(name=station['name']).first()
        if station2:
            continue
        if station['overflowStands']:
            Station.objects.create(
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
                last_update=datetime.datetime.strptime(station['lastUpdate'], '%Y-%m-%dT%H:%M:%SZ').astimezone(tz),

                total_available_bikes=station['totalStands']['availabilities']['bikes'],
                total_available_stands=station['totalStands']['availabilities']['stands'],
                total_available_mechanical_bikes=station['totalStands']['availabilities']['mechanicalBikes'],
                total_available_electrical_bikes=station['totalStands']['availabilities']['electricalBikes'],
                total_available_electrical_internal_battery_bikes=station['totalStands']['availabilities']['electricalInternalBatteryBikes'],
                total_available_electrical_removable_battery_bikes=station['totalStands']['availabilities']['electricalRemovableBatteryBikes'],
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
                overflow_available_mechanical_bikes=station['overflowStands']['availabilities']['mechanicalBikes'],
                overflow_available_electrical_bikes=station['overflowStands']['availabilities']['electricalBikes'],
                overflow_available_electrical_internal_battery_bikes=station['overflowStands']['availabilities'][
                    'electricalInternalBatteryBikes'],
                overflow_available_electrical_removable_battery_bikes=station['overflowStands']['availabilities'][
                    'electricalRemovableBatteryBikes'],
                overflow_capacity=station['overflowStands']['capacity'],

                last_schedule_run=timezone.datetime.now(tz=tz)
                )
        else:
            Station.objects.create(
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
                last_update=datetime.datetime.strptime(station['lastUpdate'], '%Y-%m-%dT%H:%M:%SZ').astimezone(tz),

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

class Migration(migrations.Migration):
    dependencies = [
        ('ellipse_bikes', '0003_insert_contracts'),
    ]

    operations = [
        migrations.RunPython(insert_station),
    ]
