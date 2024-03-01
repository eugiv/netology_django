from django.contrib import admin
from django.urls import path

from measurement.views import SensAPIList, MeasurementAPIList, SensAPIChoose

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sensors/', SensAPIList.as_view()),
    path('meas/', MeasurementAPIList.as_view()),
    path('sensor/<int:pk>/', SensAPIChoose.as_view())
]
