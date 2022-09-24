# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 20:13:52 2022

@author: sc229
"""


# IRIS Dataset KKN 
import pandas as pd
data=pd.read_csv("C:/sandhyashree/DS/ML&AI/Class/Data/IRIS.csv")
print(data.isna().sum())
print(data.head())
X=data.iloc[:,0:4].values
Y=data.iloc[:,-1].values

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
CT=ColumnTransformer([('OHE',OneHotEncoder(),["species"])],remainder="passthrough")
data=CT.fit_transform(data)

Y=Y.reshape(Y.shape[0],1)

from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=2)


from sklearn.neighbors import KNeighborsClassifier
value=[]
for i in range(1,10):
    model=KNeighborsClassifier(n_neighbors=i)
    model.fit(X_train,Y_train)
    Y_pred=model.predict(X_test)
    from sklearn.metrics import confusion_matrix
    cm=confusion_matrix(Y_test, Y_pred)
    print(cm)
    from sklearn.metrics import accuracy_score
    score=accuracy_score(Y_test,Y_pred)
    print(score)
    value.append(score)
X1=[1,2,3,4,5,6,7,8,9]
import matplotlib.pyplot as plt
plt.plot(X1,value,color='b',label='Accuracy plot')
plt.legend()
plt.show()