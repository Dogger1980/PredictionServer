import numpy as np
from django.conf import settings
from .loader import get_models
from multiprocessing import Pool
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import tensorflow as tf
    
def convert_input_data(inputData):
    """Преобразует входные данные в тензор вида (10, 1, input_length, 1). \n
       3-х мерный тензор необходим исходя из формата данных как временных рядов и особенностей работы моделей.
    """
    inputArrays = []
    
    for field in inputData:
        data = np.array(inputData[field], dtype=np.float32)
        data -= settings.MEANS[field]
        data /= settings.STDS[field]
        inputField = np.reshape(data, (1, settings.REQ_LENGTH_INPUT, 1))
        inputArrays.append(inputField)

    return inputArrays

def convert_output_data(outputData):
    """Преобразует прогноз из массивов в JSON-like словарь.
    """
    out = {}
    for key, value in zip(settings.FIELDS, outputData):
        value = np.array(value, dtype=np.float32)
        value *= settings.STDS[key]
        value += settings.MEANS[key]
        out[key] = value.tolist()

    return out

def _predict(args):
    model, inputData = args    
    pred = model.predict(inputData, batch_size=1, verbose=0)[:, -1]
    pred = np.reshape(pred, (settings.EXIT_LENGTH))
    return pred.tolist()

def predict(models, data):
    tasks = [(model, inputData) for model, inputData in zip(models, data)]
    results = []
    for task in tasks:
        results.append(_predict(task))

    return results
    
def make_prediction(inputData):
    """Создает прогноз на основе входных данных.
    """
    data = convert_input_data(inputData)
    models = get_models()
    prediction = predict(models, data)
    return convert_output_data(prediction)