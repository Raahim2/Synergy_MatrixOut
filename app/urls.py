from django.urls import path , include
from app import views
from .views import RunScanView


urlpatterns = [
    path('' , views.index),
    path('run-scan/', RunScanView.as_view(), name='run_scan'),

]

from django.contrib import admin
from django.urls import path, include


# from django.urls import path
# from .views import RunScanView

# urlpatterns = [
#     path('run-scan/', RunScanView.as_view(), name='run_scan'),
# ]