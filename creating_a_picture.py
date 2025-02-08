import cv2
import numpy as np

photo = np.zeros((300, 300, 3), dtype='uint8')

cv2.imshow('Some image', photo)
cv2.waitKey(0)