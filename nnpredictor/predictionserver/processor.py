import numpy as np
from django.conf import settings

def convert_input_data(inputData):
    """Преобразует входные данные в тензор вида (1, input_length, 1). \n
       3-х мерный тензор необходим исходя из формата данных как временных рядов и особенностей работы моделей.
    """
    inputArrays = []
    eps = 1e-3

    for field in inputData:
        data = np.array(inputData[field], dtype=np.float32)
        n = len(data)
        settings.MEANS[field] = (1 / n) * np.sum(data)
        settings.STDS[field] = np.sqrt((1 / (n - 1)) * (np.sum(dataPoint ** 2 for dataPoint in data) - n * settings.MEANS[field] ** 2))

        data -= settings.MEANS[field]
        data /= settings.STDS[field] + eps
        inputField = np.reshape(data, (1, settings.REQ_LENGTH_INPUT, 1))
        inputArrays.append(inputField)

    return inputArrays

def convert_output_data(outputData):
    """Преобразует прогноз из массивов в JSON-like словарь.
    """
    out = {}
    for field, value in zip(settings.FIELDS, outputData):
        value = np.array(value, dtype=np.float32)
        value *= settings.STDS[field]
        value += settings.MEANS[field]
        out[field] = value.tolist()

    return out