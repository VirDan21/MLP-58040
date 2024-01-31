import cv2
import numpy as np
import matplotlib.pyplot as plt


#example 1
#import cv2
#img = cv2.imread("google1.png", cv2.IMREAD_COLOR)

#cv2.imshow("google1.png",img)
#cv2.waitKey(0)
#cv2.destroyAllWindow()



#example 2
#img = cv2.imread("google1.png")

#plt.imshow(img)

#plt.waitforbuttonpress()
#plt.close('all')



#example 3

#path = r'google1.png'
#img = cv2.imread(path,cv2.IMREAD_GRAYSCALE)

#cv2.imshow('google1.png',img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()



#example 4

vid = cv2.VideoCapture(0)
while (True):

    ret,frame =vid.read()
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
       break


vid.release()
cv2.destroyAllWindows()


