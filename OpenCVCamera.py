import numpy as np
import cv2

camera = cv2.VideoCapture(0)

while True:
    ret, frame = camera.read()  # captures frame by frame
    gray = cv2.cvtColor(frame, cv2.COLOR_BAYER_BG2GRAY)  # operations on the frame
    # display the resulting fram
    cv2.imshow("frame", gray)
    if cv2.waitKey(1) and 0xFF == ord("q"):
        break


# releases camera
camera.release()
cv2.destroyAllWindows()
