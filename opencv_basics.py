# task 1
# capture pic from webcam
import cv2

web = cv2.VideoCapture(0)

ref, img = web.read()  # take snapshot from web camera object
cv2.imshow('image', img)  # figure title is image and img is the image in rgb form

cv2.waitKey(False)  # hold the image figure until user press any key from user
cv2.destroyAllWindows()

# task 2
# capture image after preview
import cv2
web = cv2.VideoCapture(0)

while 1:
    ref, img = web.read()
    cv2.imshow('image', img)
    if cv2.waitKey(True) == ord('q'):  # wait for q char
        break

web.release()  # release the webcam object
cv2.destroyAllWindows()


# task 3
# captured image save locally in hard disk
# cv2.save()
import cv2
web = cv2.VideoCapture(0)  # 0 is id for webcam

while True:
    ref, img = web.read()
    cv2.imshow('image', img)
    if cv2.waitKey(True) == ord('q'):  # wait for q char
        cv2.imwrite('demo.jpg', img)
        break

web.release()  # release the webcam object
cv2.destroyAllWindows()


















