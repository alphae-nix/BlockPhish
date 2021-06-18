# Copyright (C) 2021  DELATTE_JAILLLON_HERMANN_PERESSE-GOURBIL
#
# This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 3 of the License, or  any later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with this program; if not, go on http://www.gnu.org/licenses/gpl-3.0.html or write to the Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA

from flask import request, Flask, jsonify
import urlToArray
import xgboost as xgb
import pandas as pd
 
app = Flask(__name__)
model = xgb.XGBClassifier()
model.load_model("../deep_learning/model_xgb2_83.json")
print(model)

@app.route('/url', methods=['POST'])
def test():
    mydata = request.data.decode(encoding="UTF-8")
    urls = mydata.split(",")
    arrays = []
    for url in urls:
        array = urlToArray.urlToArray(url).getArray()
        arrays.append(array)
        
    pred = model.predict_proba(pd.DataFrame(arrays))
    preds = []
    for i in pred :
        preds.append(i[1]*100)
    print(preds)
    resp = jsonify(str(preds))
    resp.headers['Access-Control-Allow-Origin']='*'
    return resp
