from .loader import get_models
from .predictor import predict
from .processor import convert_input_data, convert_output_data
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
    
def make_prediction(inputData):
    """Создает прогноз на основе входных данных.
    """
    data = convert_input_data(inputData, compress=True)
    models = get_models()
    prediction = predict(models, data)
    return convert_output_data(prediction)