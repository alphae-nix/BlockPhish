from flask import request, Flask, jsonify
import  json 
import urlToArray

app = Flask(__name__)

# @app.route('/', methods=['GET', 'POST'])
# def getArrayServer():
#     if request.method == 'POST':
#         url = request.get_data().decode(encoding='UTF-8',errors='strict')
#         array = urlToArray.urlToArray(url).getArray()
#         #faire passer dans le reseau de neuronne !
#         return str(array)

@app.route('/test', methods=['POST'])
def test():
 print("Sum function")
 mydata = request.json
 print(mydata)
#  for key in rf.keys():
#   data=key
#   print(data)
#   data_dic=json.loads(data)
#   print(data_dic.keys())

 resp_dic='message reÃ§u'
 resp = jsonify(resp_dic)
 resp.headers['Access-Control-Allow-Origin']='*'
 return resp
