from .loader import get_models
from .predictor import predict
from .processor import convert_input_data, convert_output_data
import os
import time
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
    
def make_prediction(inputData):
    """Создает прогноз на основе входных данных.
    """
    start = time.time()
    data = convert_input_data(inputData, compress=True)
    end = time.time()
    print("convert_input_data: " + str((end - start) * 1000) + "ms", flush=True)

    start = time.time()
    models = get_models()
    end = time.time()
    print("get_models: " + str((end - start) * 1000) + "ms", flush=True)
    
    start = time.time()
    prediction = predict(models, data)
    end = time.time()
    print("predict: " + str((end - start) * 1000) + "ms", flush=True)
    
    start = time.time()
    result = convert_output_data(prediction)
    end = time.time()
    print("convert_output_data: " + str((end - start) * 1000) + "ms", flush=True)

    return result