# Copyright (C) 2021  DELATTE_JAILLLON_HERMANN_PERESSE-GOURBIL
#
# This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 3 of the License, or  any later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with this program; if not, go on http://www.gnu.org/licenses/gpl-3.0.html or write to the Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA

from flask import request, Flask, jsonify
import json 
import urlToArray
import time
from keras.models import Sequential
from keras.layers import Dense
from keras.models import model_from_json

app = Flask(__name__)


def init_ia():
    # load json and create model
    json_file = open("../deep_learning/model-15.json", 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)

     # load weights into new model
    loaded_model.load_weights("../deep_learning/model-15.h5")
    return loaded_model

def predict(model, array):
    pred=model.predict([array])
    return pred

model = init_ia()

@app.route('/', methods=['POST'])
def test():
    mydata = request.data.decode(encoding="UTF-8")
    urls = mydata.split(",")

    arrays = []
    for url in urls:
        array = urlToArray.urlToArray(url).getArray()
        arrays.append(array)
        
    pred = predict(model, arrays)

    preds = []
    for i in range(len(pred[0])):
        preds.append(pred[0][i][0])
    
    resp = jsonify(str(preds))
    resp.headers['Access-Control-Allow-Origin']='*'
    return resp
