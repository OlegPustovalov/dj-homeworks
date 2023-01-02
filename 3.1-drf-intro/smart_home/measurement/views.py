# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from django.shortcuts import render
from rest_framework.response import Response

from rest_framework.generics import RetrieveAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet

from .models import Sensor, Measurement
from .serializers import SensorSerializer, MeasurementSerializer, SensorDetailSerializer

# создание датчика и получение списка датчиков
class SensorViewSet(ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

# добавление измерения и получения списка всех измерений
class MeasurementViewSet(ModelViewSet):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
    
# вывод детальной информации по измерениям по конкретному датчику, в URL добавляется его primary key
class SensorwithmeasurementsView(RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

# обновление и удаление конкретного датчика, вывод краткой информации по нему без измерений, в URL добавляется его primary key
class SensorView(RetrieveUpdateDestroyAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

# обновление и удаление конкретного измерения, вывод информации по нему, в URL добавляется его primary key
class MeasurementView(RetrieveUpdateDestroyAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer



