# capture pic from webcam
import cv2

web = cv2.VideoCapture(0)

ref, img = web.read()
cv2.imshow('image', img)

cv2.waitKey(False)  # hold the image figure until user press any key from user
cv2.destroyAllWindows()

