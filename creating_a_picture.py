import cv2
import numpy as np

photo = np.zeros((500, 500, 3), dtype='uint8')
# BGR
# photo[100:150, 200:300] = 120, 200, 100

cv2.rectangle(photo, (50, 50), (200, 200), (120, 200, 100), thickness=cv2.FILLED)


cv2.imshow('Some image', photo)
cv2.waitKey(0)
