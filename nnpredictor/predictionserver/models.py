from django.db import models

# Create your models here.
class SensorData(models.Model):
    wellDepth     = models.JSONField(default=list, blank=False)
    bitDepth      = models.JSONField(default=list, blank=False)
    wOB           = models.JSONField(default=list, blank=False)
    hookLoad      = models.JSONField(default=list, blank=False)
    sPP           = models.JSONField(default=list, blank=False)
    flowRateIn    = models.JSONField(default=list, blank=False)
    surfaceTorque = models.JSONField(default=list, blank=False)
    surfaceRPM    = models.JSONField(default=list, blank=False)
    blockPosition = models.JSONField(default=list, blank=False)
    trippingSpeed = models.JSONField(default=list, blank=False)
    rOP           = models.JSONField(default=list, blank=False)

