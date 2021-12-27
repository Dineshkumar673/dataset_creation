# -*- coding: utf-8 -*-
"""xgboost.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Hqmj9_-KpMaYTdJ8d_rTdvwDnXo3ZjB-
"""

import numpy as np
import os
import pandas as pd

final=pd.read_csv('/mnt/fs/dataset_creation/final_data_dec11.csv')
final1=pd.read_csv('/mnt/fs/dataset_creation/islrtc_dc1row_with_labels.csv')

final1=final1.drop('class_name_1',axis=1)
#'class_name_2','class_name_3','class_name_4','class_name_5','class_name_6','class_name_7','class_name_8','class_name_9','class_name_10','class_name_11','class_name_12',
final1=final1.drop('class_name_2',axis=1)
final1=final1.drop('class_name_3',axis=1)
final1=final1.drop('class_name_4',axis=1)
final1=final1.drop('class_name_5',axis=1)
final1=final1.drop('class_name_6',axis=1)
final1=final1.drop('class_name_7',axis=1)
final1=final1.drop('class_name_8',axis=1)
final1=final1.drop('class_name_9',axis=1)
final1=final1.drop('class_name_10',axis=1)
final1=final1.drop('class_name_11',axis=1)
final1=final1.drop('class_name_12',axis=1)
#final=final.drop('Augs',axis=1)

final1 =final1[~final1.isin([np.nan, np.inf, -np.inf]).any(1)]
final =final[~final.isin([np.nan, np.inf, -np.inf]).any(1)]

X = final.iloc[:, 1:].values
y = final.iloc[:, 0].values

X_test = final1.iloc[:, 1:].values
y_test = final1.iloc[:, 0].values

#xgboost algorithm
from xgboost import XGBClassifier
xg = XGBClassifier()
xg.fit(X,y)
pred2 = xg.predict(X_test)
print("$$$XGBoost fitting Completed$$$$")

from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
matrix1=confusion_matrix(y_test, pred2)
report1=classification_report(y_test, pred2)
print(matrix1)
print(report1)
#print(confusion_matrix(y_test, y_pred1))
print(accuracy_score(y_test, pred2))
print("&&&DONE WITH ACCURACY SCORE&&&")

import pandas as pd 
pd.DataFrame(matrix1).to_csv("/mnt/fs/dataset_creation/80_class_tested_matrix_xgboost.csv")
print("$$$Done with csv$$$")
