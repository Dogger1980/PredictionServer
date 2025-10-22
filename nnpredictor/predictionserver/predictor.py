import numpy as np
from django.conf import settings

def _predict(args) -> list:
    model, inputData = args    
    pred = model.predict(inputData, batch_size=16, verbose=0)[:, -1]
    return np.reshape(pred, (settings.EXIT_LENGTH)).tolist()

def predict(models, data):
    tasks = [(model, inputData) for model, inputData in zip(models, data)]
    results = []
    for task in tasks:
        results.append(_predict(task))
    return results