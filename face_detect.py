import cv2
import numpy as np 
face_detection_model=cv2.CascadeClassifier("C:/sandhyashree/DS/cv/new/haarcascade_frontalcatface_extended.xml")
#to detect eye
#face_detection_model=cv2.CascadeClassifier("C:/Users/sc229/AppData/Local/Programs/Python/Python39/Lib/site-packages/cv2/data/haarcascade_eye_tree_eyeglasses.xml")
#to detect smile on face
#face_detection_model=cv2.CascadeClassifier("C:/Users/sc229/AppData/Local/Programs/Python/Python39/Lib/site-packages/cv2/data/haarcascade_smile.xml")

v=cv2.VideoCapture(0)
while True:
    _,image=v.read()
    image=cv2.resize(image,(600,600))
    D_face_edges=face_detection_model.detectMultiScale(image,1.3,7)
    print(len(D_face_edges))
    if len(D_face_edges)>0:
        for(x,y,w,h) in D_face_edges:
            cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)
    image=np.flip(image,1)        
    key=cv2.waitKey(1)
    if(key==ord("q")):
        cv2.destroyAllWindows()
        v.release()
        break
    cv2.imshow("detected face",image)


