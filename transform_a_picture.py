import cv2
import numpy as np

img = cv2.imread('images/Love_is.jpg')


# img = cv2.flip(img, 1)  # 0, -1
def rotate(img_shadow, angle):
    height, width = img_shadow.shape[:2]
    point = (width // 2, height // 2)
    mat = cv2.getRotationMatrix2D(point, angle, 1)
    return cv2.warpAffine(img_shadow, mat, (height, width))


# img = rotate(img, 90)

def transform(img_shadow, x, y):
    mat = np.float32([[1, 0, x], [0, 1, y]])
    return cv2.warpAffine(img_shadow, mat, (img_shadow.shape[1], img_shadow.shape[0]))


img = transform(img, 50, 100)

cv2.imshow('super_picture', img)

cv2.waitKey(0)
