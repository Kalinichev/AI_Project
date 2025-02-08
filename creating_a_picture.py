import cv2
import numpy as np

photo = np.zeros((500, 500, 3), dtype='uint8')
photo[:] = 255, 0, 0

cv2.imshow('Some image', photo)
cv2.waitKey(0)