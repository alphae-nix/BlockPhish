# Copyright (C) 2021  DELATTE_JAILLLON_HERMANN_PERESSE-GOURBIL
#
# This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 3 of the License, or  any later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with this program; if not, go on http://www.gnu.org/licenses/gpl-3.0.html or write to the Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA


import pandas as pd
import numpy as np

from sklearn.model_selection import KFold
import xgboost as xgb

from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score

def binary_classification_accuracy(actual, pred):
    
    print(f'Confusion matrix: \n{confusion_matrix(actual, pred)}')
    print(f'Accuracy score: \n{accuracy_score(actual, pred)}')
    print(f'Classification report: \n{classification_report(actual, pred)}')



l_good = pd.read_pickle('good_url_save3.p')
l_good = [x + [1] for x in l_good]

l_good2 = pd.read_pickle('good_url_save2.p')
l_good2 = [x + [1] for x in l_good2]

l_bad = pd.read_pickle('bad_url_save2.p')
l_bad = [y + [0] for y in l_bad]

df_good = pd.DataFrame(l_good,columns=['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','result'])
df_good2 = pd.DataFrame(l_good2,columns=['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','result'])
df_bad =pd.DataFrame(l_bad,columns=['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','result'])

df = pd.concat([df_good,df_bad,df_good2])

target = df['result']
features = df.drop(columns=['result'])

folds = KFold(n_splits=4, shuffle=True, random_state=42)

train_index_list = list()
validation_index_list = list()

for fold, (train_idx, validation_idx) in enumerate(folds.split(features, target)):   
    model = xgb.XGBClassifier(base_score=0.5)
    model.fit(np.array(features)[train_idx,:], np.array(target)[train_idx])
    predicted_values = model.predict(np.array(features)[validation_idx,:])
    print(f'==== FOLD {fold+1} ====')
    binary_classification_accuracy(np.array(target)[validation_idx], predicted_values)

print(model)

model.save_model("model_xgb2_83.json")
