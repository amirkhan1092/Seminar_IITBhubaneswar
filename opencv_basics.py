# capture pic from webcam
import cv2

web = cv2.VideoCapture(0)

ref, img = web.read()  # take snapshot from web camera object
cv2.imshow('image', img)  # figure title is image and img is the image in rgb form

cv2.waitKey(False)  # hold the image figure until user press any key from user
cv2.destroyAllWindows()




