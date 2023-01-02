from django.contrib import admin
from django.urls import path

from rest_framework.routers import DefaultRouter
from measurement.views import SensorViewSet, MeasurementViewSet, MeasurementView, SensorView,SensorwithmeasurementsView

r1 = DefaultRouter()
r1.register ('sensor',SensorViewSet)

r2 = DefaultRouter()
r2.register ('measurement', MeasurementViewSet)


urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('admin/', admin.site.urls),
    path('measure/<pk>/', MeasurementView.as_view()),
    path('sens/<pk>/', SensorView.as_view()),
    path('sensors/<pk>/', SensorwithmeasurementsView.as_view()),
]+ r1.urls+r2.urls

