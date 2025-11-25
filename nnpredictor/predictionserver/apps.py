from django.apps import AppConfig
from django.conf import settings
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

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
        from .processor import convert_input_data

        dummy_data = np.random.uniform(0, 1, (len(settings.FIELDS), settings.REQ_LENGTH_INPUT))
        dummy_dict = {}
        for idx, field in enumerate(settings.FIELDS):
            dummy_dict[field] = dummy_data[idx]

        dummy_data, MEANS, STDS = convert_input_data(dummy_dict, compress=True)
        models = get_models()
        predict(models, dummy_data)
        
