# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 20:19:46 2022

@author: sc229
"""

import pandas as pd
data=pd.read_csv("C:/sandhyashree/DS/ML&AI/Class/Data/heart.csv")
print(data.isna().sum())
print(data.head())
x1=data.corr()

X=data.iloc[:,0:13].values
Y=data['target'].values
Y=Y.reshape(Y.shape[0],1)

from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
X=sc.fit_transform(X)

from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=.2,random_state=23)

from sklearn.linear_model import LogisticRegression
log=LogisticRegression()
log.fit(X_train,Y_train)
Y_pred=log.predict(X_test)

# to find the accuracy of the model
from sklearn.metrics import confusion_matrix
cm=confusion_matrix(Y_test, Y_pred)
print(cm)

from sklearn.metrics import accuracy_score
acc=accuracy_score(Y_test,Y_pred)
print(acc)
