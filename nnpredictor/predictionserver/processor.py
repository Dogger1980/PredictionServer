import numpy as np
from django.conf import settings

def convert_input_data(inputData, compress = False, compressionCoeff = 30):
    """Преобразует входные данные в тензор вида (1, input_length, 1). \n
       3-х мерный тензор необходим исходя из формата данных как временных рядов и особенностей работы моделей.
    """
    inputArrays = []
    eps = 1e-3

    for field in inputData:
        data = np.array(inputData[field], dtype=np.float32)
        n = len(data)
        settings.MEANS[field] = (1 / n) * sum(data)
        settings.STDS[field] = np.sqrt(
            (1 / (n - 1)) * sum(dataPoint - settings.MEANS[field] for dataPoint in data) ** 2
            )

        data -= settings.MEANS[field]
        data /= settings.STDS[field] + eps
        if compress: 
            data = _compress_data(data, compressionCoeff)
            inputField = np.reshape(data, (1, settings.REQ_LENGTH_INPUT // compressionCoeff, 1))
        else:
            inputField = np.reshape(data, (1, settings.REQ_LENGTH_INPUT, 1))
        inputArrays.append(inputField)

    return inputArrays

def _compress_data(data, coeff = 30):
    """## Алгоритм сжатия данных. \n
       Только для использования внутри модуля `processor.py`. \n
       ## Принцип работы: \n
       coeff * 2 точек временного ряда распадаются на две части, по coeff каждая, \n
       и сжимаются в 2 точки, причем в зависимости от "топологии" ряда:
       - если во второй части сначала минимальный элемент этой части, а затем максимальный, \n
         то первая точка становится минимальным элементом coeff * 2 отрезка, вторая —\n
         максимальным второй части; \n
       - иначе первая точка становится максимальным элементом coeff * 2 отрезка, вторая —\n
         минимальным второй части. \n
       ## Входные данные: \n
       - data - массив данных (один из временных рядов) \n
       - coeff - коэффициент сжатия \n
       ## Выходные данные: \n
       - compressedData - сжатый массив данных
    """
    compressedData     = np.zeros(len(data) // coeff)
    compressedData[0]  = data[0]
    compressedData[-1] = data[-1]

    for i, start in zip(
        range(1, len(compressedData) - 1, 2), 
        range(0, len(data), coeff * 2)):

        if (i + 1) < len(compressedData):
            pt1 = data[start         : start + coeff]
            pt2 = data[start + coeff : start + coeff * 2]

            maxPt1, minPt1 = np.max(pt1),    np.min(pt1)
            maxPt2, minPt2 = np.max(pt2),    np.min(pt2)
            idxMax, idxMin = np.argmax(pt2), np.argmin(pt2)

            if idxMin < idxMax:
                compressedData[i]     = minPt2 if minPt2 < minPt1 else minPt1
                compressedData[i + 1] = maxPt2
            else:
                compressedData[i]     = maxPt2 if maxPt2 > maxPt1 else maxPt1
                compressedData[i + 1] = minPt2

    return compressedData

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