import os
import cv2
import numpy as np

def get_list_of_files(basepath):
    filelist=os.listdir(basepath)
    all_files_list=[]
    for folder_name in filelist:
        fullpath=os.path.join(basepath,folder_name)
        if os.path.isdir(fullpath):
            all_files_list=all_files_list+get_list_of_files(fullpath)
        else:
            all_files_list.append(fullpath)
    return all_files_list

image_path_list=get_list_of_files(r'C:/sandhyashree/DS/cv/new/dataset')

lable_data=[]
image_list=[]
for img in image_path_list:
    lable=os.path.split(os.path.split(img)[0])[1]
    lable_data.append(lable)
    i = cv2.imread(img)
    i=cv2.resize(i,(32,32))
    image_list.append(i)
lable_data=np.array(lable_data)
image_data=np.array(image_list)
data =image_data.reshape(image_data.shape[0],image_data.shape[1]*image_data.shape[2]*image_data.shape[3])
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(data,lable_data,test_size=.20,random_state=2)

#Logistic regression
from sklearn.linear_model import LogisticRegression 
log=LogisticRegression()
log.fit(x_train,y_train)
y_pred=log.predict(x_test)

from sklearn.metrics import accuracy_score
acc=accuracy_score(y_test,y_pred)
print("logistic",acc)

#KNN
from sklearn.neighbors import KNeighborsClassifier
value=[]
for i in range(1,10):
    model12=KNeighborsClassifier(n_neighbors=i)
    model12.fit(x_train,y_train)
    y_pred6=model12.predict(x_test)

    from sklearn.metrics import accuracy_score
    score=accuracy_score(y_test,y_pred6)
    value.append(score)
print("KNN with 1 to 10 neighbours",value)

#SVC
from sklearn.svm import SVC
model=SVC(kernel="linear",random_state=0) #50 per
model1=SVC(kernel="rbf",random_state=0) #61.9 per(highest of all)
model2=SVC(kernel="poly",random_state=0) #60 per
model.fit(x_train,y_train)
model1.fit(x_train,y_train)
model2.fit(x_train,y_train)
y_pred3=model.predict(x_test)
y_pred1=model1.predict(x_test)
y_pred2=model2.predict(x_test)
from sklearn.metrics import accuracy_score
acc1=accuracy_score(y_test,y_pred3)
print("svm -linear",acc1)
acc2=accuracy_score(y_test,y_pred1)
print("svm - rbf",acc2)
acc3=accuracy_score(y_test,y_pred2)
print("svm -poly",acc3)

#Decision Tree 
Max_depth=[]
from sklearn.tree import DecisionTreeClassifier
for i in range(1,10):
    model=DecisionTreeClassifier(max_depth=i)
    model.fit(x_train,y_train)
    y_pred4=model.predict(x_test)

    from sklearn.metrics import accuracy_score
    score=accuracy_score(y_test,y_pred4)
    Max_depth.append(score)
print("DTC for 10 Max depths",Max_depth)

# Random forest
from sklearn.ensemble import RandomForestClassifier as r
estimator=[]
for i in range (1,10):
    model=r(n_estimators=i,random_state=2)
    model.fit(x_train,y_train)
    y_pred5=model.predict(x_test)

    from sklearn.metrics import accuracy_score
    score=accuracy_score(y_pred5,y_test)
    estimator.append(score)
print("Random forest with 10 estimators",estimator)



