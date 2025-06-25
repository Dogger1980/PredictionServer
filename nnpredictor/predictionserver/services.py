import numpy as np
from django.conf import settings
from .apps import PredictionserverConfig
from .loader import get_model
    
def convert_input_data(inputData):
    inputArrays = []
    
    for field in inputData:
        inputArrays.append(inputData[field])

    input_array = np.array(inputArrays).T
    input_array = np.reshape(input_array, (1, input_array.shape[0], input_array.shape[1]))
    return input_array.astype('float32')

def convert_output_data(outputData):
    outputArrays = np.reshape(outputData, (settings.EXIT_LENGTH, settings.FEATURES_TOTAL))
    outputArrays = outputArrays.T
    out = {}
    for key, value in zip(settings.FIELDS, outputArrays):
        out[key] = value.tolist()

    return out
    
def make_prediction(inputData):
    data = convert_input_data(inputData)
    model = get_model()
    prediction = model.predict(data)
    return convert_output_data(prediction)