import cv2
import numpy as np

img = cv2.imread('images/Wet_street.jpg')
img = cv2.resize(img, (img.shape[1] // 2, img.shape[0] // 2))
img = cv2.GaussianBlur(img, (3, 3), 0)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = cv2.Canny(img, 190, 190)

kernel = np.ones((5, 5), np.uint8)
img = cv2.dilate(img, kernel, iterations=1)
img = cv2.erode(img, kernel, iterations=1)

cv2.imshow('Wet street', img)
print(img.shape)
cv2.waitKey(0)

# cap = cv2.VideoCapture('videos/Hahaha.mp4')
#
# while True:
#     success, img = cap.read()
#     cv2.imshow('Hahaha', img)
#
#     if cv2.waitKey(5) & 0xFF == ord('q'):
#         break
