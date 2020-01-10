from keras.models import model_from_json
import json
import src.constants as const
import numpy as np

def loadModel():
    with open('./'+const.MODEL_ROUTE+const.MODEL+'.h5.json','r') as f:
        model_json = json.load(f)

    model = model_from_json(model_json)
    model.load_weights('./'+const.MODEL_ROUTE+const.MODEL+'.h5')
    return model


