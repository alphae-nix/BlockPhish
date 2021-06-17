# Copyright (C) 2021  DELATTE_JAILLLON_HERMANN_PERESSE-GOURBIL
#
# This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 3 of the License, or  any later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with this program; if not, go on http://www.gnu.org/licenses/gpl-3.0.html or write to the Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA

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
