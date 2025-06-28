from tensorflow.keras.models import load_model
from django.conf import settings
import os

_model = None

def model_loader():
    """Загружает модель для прогнозирования с помощью tensorflow.keras.models.load_model.
       Если не получается, то возвращает ошибку ValueError"""
    global _model
    if _model is None:
        modelPath = os.path.join(settings.MODEL_DIR, 'cnn.keras')
        if modelPath.endswith(".keras"):
            _model = load_model(modelPath)
        else:
            raise ValueError(f"Неподдерживаемый формат модели, либо модели нет в папке {modelPath}")

def get_model():
    """Возвращает уже загруженную модель
    """
    return _model