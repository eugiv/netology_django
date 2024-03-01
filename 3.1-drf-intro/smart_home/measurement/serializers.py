from rest_framework import serializers

from measurement.models import Sensor, Measurement


class MeasurementsSerializer(serializers.ModelSerializer):
    sens_id = serializers.PrimaryKeyRelatedField(queryset=Sensor.objects.all(), required=False, write_only=True)

    class Meta:
        model = Measurement
        fields = ['sens_id', 'temperature', 'created_at', 'picture']


class SensorSerializer(serializers.ModelSerializer):
    measurements = MeasurementsSerializer(many=True, read_only=True)

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'descr', 'measurements']
