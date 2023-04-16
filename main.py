import cv2
import numpy as np

cap = cv2.VideoCapture(0)

image = cv2.imread("The-Grand-Palace-Bangkok.png")

while True:
    ret, frame = cap.read()

    image = cv2.resize(image, (640, 480))
    frame = cv2.resize(frame, (640, 480))

    l_black = np.array([0, 0, 0])
    u_black = np.array([70, 70, 70])

    mask = cv2.inRange(frame, l_black, u_black)
    res = cv2.bitwise_and(frame, frame, mask = mask)

    final = frame - res
    final = np.where(final == 0, image, final)

    cv2.imshow("Invisible Cloak", final)

    if cv2.waitKey(1) == 27 or cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
