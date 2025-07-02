from django.apps import AppConfig
from django.conf import settings


class PredictionserverConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'predictionserver'
    
    def ready(self):
        """Загружает модель при старте приложения
        """
        import os
        if os.environ.get('RUN_MAIN') or not os.environ.get('DJANGO_AUTORELOAD'):
            from .loader import models_loader
            models_loader()
        
