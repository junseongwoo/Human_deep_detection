import cv2
import matplotlib.pyplot as plt
from deepface import DeepFace

cap = cv2.VideoCapture(0) 
faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_frontalface_default.xml')

while True:
    ret, frame = cap.read()
    prediction = DeepFace.analyze(frame)
    faces = faceCascade.detectMultiScale(frame, 1.1, 4)

    for (x, y, u, v) in faces:
        cv2.rectangle(frame, (x,y), (x+u, y+v), (0, 0, 225), 2)
    cv2.imshow('test', frame)

    k = cv2.waitKey(1)
    if k == 27:
        break

cap.release()

cv2.destroyAllWindows