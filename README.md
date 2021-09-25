# HomeApp
Django API with basic CRUD funtionality

##Getting Started

### Install packages
configure you virtenv of choice and install reuirments.txt

```
pip install requirents.txt
```
### Django Dev Server
From HomeApp Directory. Setup migrations for default SQLite3 db
```
python manage.py makemigrations
python manage.py migrate

```
### Start Dev Server
```
python manage.py runserver
```

## Endpoints http://(http://localhost:8000/api/
## Root
*http://http://localhost:8000/api/*

### NewDevice
/create-device/
*example*
```
{
    "id": 1,
    "title": "Light 1",
    "isThermostat": false,
    "isLight": true,
    "is_on": true,
    "tempature": "0"
}
```
### AllDevice
/all-device/
*Endpoint returns all devices*

### AllDeviceHistory
/all-device-history/
*example*
```

```
### DeviceHistory
/device-history/
*example*
*Note device_id id is device.id as foregin key will return all activity for device*
```
{
    "id": 4,
    "update_time": "2021-09-25T19:57:22.255835Z",
    "isThermostat": false,
    "isLight": true,
    "isOn": false,
    "tempature": "0",
    "device_id": 1
}
```
### UpdateDeviceStatus
update-device-status/<str:id>/
*example /api/device-status/1/*

```
{
    "id": 4,
    "isThermostat": false,
    "isLight": true,
    "isOn": false,
    "tempature": "0",
}
```
### DeleteDevice
/delete-device/<str:id>/
*example*
*/delete-device/1/*
```

```