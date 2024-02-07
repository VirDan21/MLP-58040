import numpy as np
import cv2 as cv

#cap = cv.VideoCapture(0)



#if not cap.isOpened():
  #  print("Cannot open camera")
   # exit()

#while True:

   # ret, frame = cap.read()


   # print("Frame capture status:", ret)


   # if not ret:
      #  print("Can't receive frame (stream end?). Exiting ...")
     #   break


   # gray_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)


   # cv.imshow('Grayscale Frame', gray_frame)

  #  if cv.waitKey(1) == ord('q'):
    #    break


#cap.release()
#cv.destroyAllWindows()




cap = cv.VideoCapture(0)

fourcc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter('output.mp4v', fourcc, 20.0, (640, 480))
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    cv.imshow('frame', frame)
    out.write(frame)
    if cv.waitKey(1) == ord('q'):
        break

cap.release()
out.release()
cv.destroyAllWindows()

cap = cv.VideoCapture('output.mp4v')
while cap.isOpened():
        ret, frame = cap.read()
       # if frame is read correctly ret is true
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        cv.imshow('frame', frame)
        if cv.waitKey(1) == ord ('w'):
            break
cap.release()
cv.destroyAllWindows()
