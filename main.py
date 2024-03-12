import cv2
from cvzone.HandTrackingModule import HandDetector


cap = cv2.VideoCapture(0)
cap.set(3, 350)
cap.set(4, 280)

detector = HandDetector(detectionCon=1)

while True:
    imBg = cv2.imread("resources/bg.png")
    success, img = cap.read()

    imgScaled = cv2.resize(img, (280, 280))

    row_offset = 80
    col_offset = 80

    start_row = 233 - row_offset
    end_row = start_row + imgScaled.shape[0]
    start_col = 560 - col_offset
    end_col = start_col + imgScaled.shape[1]

    # Find the hand and its landmarks
    hands, img = detector.findHands(imgScaled)

    imBg[start_row:end_row, start_col:end_col] = imgScaled

    cv2.imshow("Image", img)
    cv2.imshow("Background", imBg)
    cv2.imshow("Scaled", imgScaled)

    cv2.waitKey(1)
