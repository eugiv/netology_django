from django.contrib import admin
from django.urls import path

from measurement.views import SensAPIList, MeasurementAPIList, SensAPIChoose

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sensors/', SensAPIList.as_view()),
    path('measures/', MeasurementAPIList.as_view()),
    path('sensors/<int:pk>/', SensAPIChoose.as_view())
]
