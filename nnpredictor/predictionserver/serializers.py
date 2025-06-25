from rest_framework import serializers
from .models import SensorData
from django.conf import settings
required_length = settings.REQ_LENGTH_INPUT

class SensorSerializer(serializers.ModelSerializer):
    wellDepth     = serializers.ListField(allow_empty=False, child=serializers.FloatField(), max_length=required_length, min_length=required_length),
    bitDepth      = serializers.ListField(allow_empty=False, child=serializers.FloatField(), max_length=required_length, min_length=required_length),
    wOB           = serializers.ListField(allow_empty=False, child=serializers.FloatField(), max_length=required_length, min_length=required_length),
    hookLoad      = serializers.ListField(allow_empty=False, child=serializers.FloatField(), max_length=required_length, min_length=required_length),
    sPP           = serializers.ListField(allow_empty=False, child=serializers.FloatField(), max_length=required_length, min_length=required_length),
    flowRateIn    = serializers.ListField(allow_empty=False, child=serializers.FloatField(), max_length=required_length, min_length=required_length),
    surfaceTorque = serializers.ListField(allow_empty=False, child=serializers.FloatField(), max_length=required_length, min_length=required_length),
    surfaceRPM    = serializers.ListField(allow_empty=False, child=serializers.FloatField(), max_length=required_length, min_length=required_length),
    blockPosition = serializers.ListField(allow_empty=False, child=serializers.FloatField(), max_length=required_length, min_length=required_length),
    trippingSpeed = serializers.ListField(allow_empty=False, child=serializers.FloatField(), max_length=required_length, min_length=required_length),
    rOP           = serializers.ListField(allow_empty=False, child=serializers.FloatField(), max_length=required_length, min_length=required_length)

    class Meta:
        model = SensorData
        fields = "__all__"