import cv2

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

cap = cv2.VideoCapture(0)

while True:
    success, image = cap.read()
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    data = face_cascade.detectMultiScale(img_gray, 1.1, 19)
    for (x, y, z, v) in data:
        cv2.rectangle(image, (x, y), (x + z, y + v), (0, 255, 0), 2)

    cv2.imshow('web', image)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
