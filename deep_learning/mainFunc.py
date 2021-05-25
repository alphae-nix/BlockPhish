#/usr/bin/python3
import urlToArray
from urllib.parse import urlparse
import sys
import os

from keras.models import Sequential
from keras.layers import Dense
from keras.models import model_from_json

def main():
     objet = urlToArray.urlToArray(sys.argv[1]).getArray()
     print(objet)
     print(objet.shape)
     
     cmd = "wget -nc https://perso.esiee.fr/~delattel/projetE3/model.json https://perso.esiee.fr/~delattel/projetE3/model.h5"
     os.system(cmd)

     # load json and create model
     json_file = open('model.json', 'r')
     loaded_model_json = json_file.read()
     json_file.close()
     loaded_model = model_from_json(loaded_model_json)

     # load weights into new model
     loaded_model.load_weights("model.h5")
     print("Loaded model from disk") 

     # prédiction à partir du modèle
     pred=loaded_model.predict(objet)
     print(pred)

     return pred

if __name__ == "__main__":
     main()