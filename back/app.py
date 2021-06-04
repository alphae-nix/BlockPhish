from flask import request, Flask, jsonify
import json 
import urlToArray

from keras.models import Sequential
from keras.layers import Dense
from keras.models import model_from_json

app = Flask(__name__)


def init_ia():
    # load json and create model
     json_file = open('../deep_learning/model.json', 'r')
     loaded_model_json = json_file.read()
     json_file.close()
     loaded_model = model_from_json(loaded_model_json)

     # load weights into new model
     loaded_model.load_weights("../deep_learning/model.h5")
     print("Loaded model from disk") 
     return loaded_model

def predict(model, array):
     pred=model.predict(array)
     print(pred)
     return pred

model = init_ia()

@app.route('/test', methods=['POST'])
def test():
    mydata = request.data.decode(encoding="UTF-8")
    array = mydata.split(",")
    array2 = urlToArray.urlToArray(array[0]).getArray()
    pred = predict(model,array2)
    print(pred)

    resp = jsonify(pred)
    resp.headers['Access-Control-Allow-Origin']='*'
    return resp
