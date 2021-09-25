from django.core.exceptions import ValidationError
from django.db import models
from django.db.models.deletion import CASCADE
from django.utils import timezone

# Sanity Checker for Temp
def validate_temp(temp):
    int_temp = int(temp)
    if int_temp < 101 and int_temp > 0:
        return str(int_temp)
    else:
        return str(0)


class Device(models.Model):
    title = models.CharField(max_length=200)
    isThermostat = models.BooleanField(default=False)
    isLight = models.BooleanField(default=False)
    is_on = models.BooleanField(default=False)
    tempature = models.CharField(max_length=200, validators=[validate_temp])
    def __str__(self):
        return self.title

class LogAction(models.Model):
    device_id = models.ForeignKey(Device, on_delete=models.CASCADE)
    update_time = models.DateTimeField(default=timezone.now)
    isThermostat = models.BooleanField(default=False)
    isLight = models.BooleanField(default=False)
    isOn = models.BooleanField(default=False)
    if isThermostat:
        tempature = models.CharField(max_length=3, validators=[validate_temp])
    else:
        tempature = models.CharField(max_length=3, default="0")

    def __str__(self):
        return self.device_id, self.update_time, self.isThermostat, self.isLight, self.isOn, self.tempature

