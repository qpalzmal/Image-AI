'''
Template is taken from https://gist.github.com/tedmiston/6060034
Uses webcam and displays what it captures
Modified to be used in conjunction with WebcamObjectDetection.py
'''

import cv2
# import asyncio

camera = cv2.VideoCapture(0)


def show_webcam(cam):
    # while True:  # used to show the webcam capture indefinitely
    ret, frame = cam.read()  # captures frame by frame
    frame = cv2.flip(frame, 1)
    # display the resulting frame
    # cv2.imshow("Webcam", frame)
    cv2.imwrite("image.png", frame)

    cv2.waitKey(2000)  # waits the given amount of seconds 1000 = 1 sec
    # if cv2.waitKey(27) == 27:  # esc key to close - to be used with the while loop
    #     break

    camera.release()
    cv2.destroyAllWindows()


def main():
    show_webcam(cam=camera)


if __name__ == "__main__":
    main()
