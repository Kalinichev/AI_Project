import cv2

img = cv2.imread('images/Wet_street.jpg')
img = cv2.resize(img, (img.shape[1] // 2, img.shape[0] // 2))

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
