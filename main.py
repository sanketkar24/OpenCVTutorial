import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)
#print(img)
#img[:]= 255,0,0

cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),5)
cv2.rectangle(img,(0,0),(250,300),(255,255,0),9)
cv2.circle(img,(300,300),30,(255,100,0),3)
cv2.putText(img,"OPEN CV FIRST", (100,100),cv2.FONT_ITALIC,1,(240,225,0),1)


cv2.imshow("Image",img)
cv2.waitKey(0)