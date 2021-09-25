from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views


urlpatterns = [
    path('', views.apiOverview, name="api-overview"),
    path('all-device/', views.allDevices, name="all-device"),
    path('create-device/', views.newDevice, name="create-device"),
    path('update-device-status/', views.updateDeviceHistory, name="update-device-status"),
    path('all-device-history/', views.allDeviceHistory, name="all-device-history"),
    path('device-history/<str:id>/', views.deviceHistory, name="device-history"),
    path('delete-device/<str:id>/', views.deleteDevice, name="delete-device")

]
