import cv2
import cvzone

cap = cv2.VideoCapture(0)
cap.set(3, 650)
cap.set(4, 480)


while True:
    imBg = cv2.imread("resources/bg.png")
    success, img = cap.read()

    imgScaled = cv2.resize(img, (0, 0), None, 0.5, 0.5)
    imgScaled = imgScaled[:, 80:480]

    imBg[233:473, 560:795] = imgScaled

    cv2.imshow("Image", img)
    cv2.imshow("Background", imBg)
    cv2.imshow("Scaled", imgScaled)

    cv2.waitKey(1)