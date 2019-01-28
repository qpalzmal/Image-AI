# Taken from https://gist.github.com/tedmiston/6060034
# Uses webcam and displays what it captures
import cv2


def show_webcam(mirror=False):
    camera = cv2.VideoCapture(0)
    while True:
        ret, frame = camera.read()  # captures frame by frame
        if mirror:
            frame = cv2.flip(frame, 1)
        # display the resulting frame
        cv2.imshow("Webcam", frame)
        if cv2.waitKey(27):
            break  # esc to quit
    camera.release()
    cv2.destroyAllWindows()


def main():
    show_webcam(mirror=True)


if __name__ == "__main__":
    main()
