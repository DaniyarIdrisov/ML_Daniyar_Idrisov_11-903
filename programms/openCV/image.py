import cv2

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

image = cv2.imread("zidane.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

data = face_cascade.detectMultiScale(image, 1.1, 19)
for (x, y, z, v) in data:
    cv2.rectangle(image, (x, y),
                  (x + z, y + v), (0, 255, 0), 2)

cv2.imshow('image', image)
cv2.waitKey()
