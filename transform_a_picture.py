import cv2
import numpy as np

img = cv2.imread('images/Love_is.jpg')

img = cv2.flip(img, 1)

cv2.imshow('Картинище', img)

cv2.waitKey(0)
