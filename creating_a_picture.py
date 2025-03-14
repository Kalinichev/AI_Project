import cv2
import numpy as np

photo = np.zeros((500, 500, 3), dtype='uint8')
# BGR
# photo[100:150, 200:300] = 120, 200, 100

cv2.rectangle(photo, (50, 50), (200, 200), (120, 200, 100), thickness=cv2.FILLED)
cv2.line(photo, (0, photo.shape[0] // 2), (photo.shape[1], photo.shape[1] // 2), (20, 240, 220), thickness=4)
cv2.circle(photo, (photo.shape[1] // 2, photo.shape[0] // 2), 60, (25, 25, 240), thickness=cv2.FILLED)
cv2.putText(photo, 'Liza-kisa))', (270, 150), cv2.FONT_HERSHEY_TRIPLEX, 1, (175, 25, 240), 2)

cv2.imshow('Some image', photo)
cv2.waitKey(0)
