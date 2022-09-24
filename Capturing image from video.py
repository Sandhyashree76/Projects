import cv2
import numpy as np
cap=cv2.VideoCapture(0)
while True:
    _,frame=cap.read()
    frame=cv2.resize(frame,(500,500))
    cv2.imshow("live image",frame)
    ch=cv2.waitKey(1)
    if (ch==ord("q")):
        break
    if(ch==ord("c")):
        cv2.imwrite("Video_image.jpg",frame)
cap.release()
cv2.destroyAllWindows()
        
