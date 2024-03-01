from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.views.static import serve

from measurement.views import SensAPIList, MeasurementAPIList, SensAPIChoose

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sensors/', SensAPIList.as_view()),
    path('measurements/', MeasurementAPIList.as_view()),
    path('sensors/<int:pk>/', SensAPIChoose.as_view()),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
