import cv2

# img = cv2.imread('images/Wet_street.jpg')
# cv2.imshow('Wet street', img)
#
# cv2.waitKey(0)

cap = cv2.VideoCapture('videos/Hahaha.mp4')

while True:
    success, img = cap.read()
    cv2.imshow('Hahaha', img)

    if cv2.waitKey(5) & 0xFF == ord('q'):
        break
