# Taken from https://gist.github.com/tedmiston/6060034
# Uses webcam and displays what it captures
import cv2
import time
# import asyncio

camera = cv2.VideoCapture(0)


# def show_webcam(cam, mirror=False):
#     while True:
#         ret, frame = cam.read()  # captures frame by frame
#         if mirror:
#             frame = cv2.flip(frame, 1)
#         # display the resulting frame
#         cv2.imshow("Webcam", frame)
#
#         # print("TRY TIME SLEEP")
#         # time.sleep(1)
#         # print("DONE TIME SLEEP")
#         # print("")
#         # print("TRY ASYNCIO SLEEP")
#         # await asyncio.sleep(1)
#         # print("DONE ASYNCIO SLEEP")
#         # print("")
#
#         if cv2.waitKey(27) == 27:
#             break  # esc to quit
#     cam.release()
#     cv2.destroyAllWindows()


def show_webcam(cam, mirror=False):
    ret, frame = cam.read()  # captures frame by frame
    if mirror:
        frame = cv2.flip(frame, 1)
    # display the resulting frame
    cv2.imshow("Webcam", frame)

    # time.sleep(3)

    # functions similar to time.sleep but doesn't suspend webcam
    old_time = time.time()
    current_time = 0
    while current_time - old_time <= 3:
        current_time = time.time()
        print(current_time, "CURRENT")
        print(old_time, "OLD")

    # cam.release()
    cv2.destroyAllWindows()


def main():
    show_webcam(cam=camera, mirror=True)


if __name__ == "__main__":
    main()
