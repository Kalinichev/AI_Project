import cv2
import numpy as np

cap = cv2.VideoCapture('videos/Hahaha.mp4')

while True:
    success, img = cap.read()

    img = cv2.GaussianBlur(img, (9, 9), 3)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.Canny(img, 75, 75)

    cv2.imshow('Super Hahaha', img)
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break
