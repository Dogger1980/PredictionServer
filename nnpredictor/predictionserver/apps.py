from django.apps import AppConfig
from django.conf import settings


class PredictionserverConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'predictionserver'
    model = None

    def ready(self):
        import os
        if os.environ.get('RUN_MAIN') or not os.environ.get('DJANGO_AUTORELOAD'):
            from .loader import model_loader
            model_loader()
        
