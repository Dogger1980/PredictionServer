from django.apps import AppConfig
from django.conf import settings 


class PredictionserverConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'predictionserver'
    
    def ready(self):
        """Загружает модели при старте приложения
        """
        import os
        if os.environ.get('RUN_MAIN') or not os.environ.get('DJANGO_AUTORELOAD'):
            from .loader import models_loader
            models_loader()
            PredictionserverConfig.cold_start(self)

    def cold_start(self):
        """Запускает предсказания при старте приложения для ускорения первого запроса
        """
        import numpy as np
        from .loader import get_models
        from .services import predict
        dummy_data = np.random.uniform(0, 0, (10, 1, 600, 1))
        models = get_models()
        predict(models, dummy_data)
        
