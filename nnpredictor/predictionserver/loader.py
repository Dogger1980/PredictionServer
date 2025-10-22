from tensorflow.keras.models import load_model
from django.conf import settings
from django.conf import settings
import os

_models = []

def models_loader():
    """Загружает модели для прогнозирования с помощью tensorflow.keras.models.load_model.
       Если не получается, то возвращает ошибку ValueError"""
    global _models
    num_models = len(settings.FIELDS)
    for i in range(0, num_models):
        modelPath = os.path.join(settings.MODELS_DIR, f'wmodel_checkpoint{i + 1}.keras')
        try:
            _models.append(load_model(modelPath))
        except:
            raise ValueError(f"Неподдерживаемый формат моделей, либо моделей нет по адресу {modelPath}")

def get_models():
    """Возвращает уже загруженные модели
    """
    return _models