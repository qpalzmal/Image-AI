'''
Program that uses a trained model to detect objects that are captured by the video capture device
Requires OpenCVCamera.py and (TRAINED MODEL) - both are found at https://github.com/qpalzmal/Image-Object-Recognition
Contains traces of experimental asynchronous programming - ignore for now
C:\\Users\\(PLACEHOLDER)\\AppData\\Local\\Programs\\Python\\Python36\\Scripts - ignore - used for pyinstaller
'''

from imageai.Detection import VideoObjectDetection
import OpenCVCamera as cv
# import asyncio

detector = VideoObjectDetection()
detector.setModelTypeAsRetinaNet()
detector.setModelPath("resnet50_coco_best_v2.0.1.h5")

# 1 = bad ---- 5 = good
# detector.loadModel(detection_speed="normal")  # 1 speed 5 accuracy
detector.loadModel(detection_speed="faster")  # 3 speed 3 accuracy
# detector.loadModel(detection_speed="flash")  # 5 speed 1 accuracy


# per_frame_function passes in all of the present parameters
def EveryFrame(frame_number, output_array, output_count):
    # cv.main()  # displays the image that is captured by the webcam
    # print(output_array)  # prints out each individual object, name, and box location
    print(output_count)  # prints out the unique count for different objects
    print("")


# calling a async function returns a coroutine object and doesn't run them
def DetectObjects():
    detector.detectObjectsFromVideo(output_file_path="Videos\\WEBCAM",
                                    frames_per_second=15,  # LAPTOP WEBCAM RUNS AT 30 FPS
                                    minimum_percentage_probability=50,
                                    log_progress=True,
                                    camera_input=cv.camera,
                                    per_frame_function=EveryFrame)


def main():
    # loop = asyncio.new_event_loop()

    # detect_task = loop.create_task(DetectObjects())
    # show_webcam_task = loop.create_task(cvcamera.main())

    # loop.run_until_complete(detect_task)
    # loop.run_until_complete(show_webcam_task)

    # await DetectObjects()
    DetectObjects()


if __name__ == "__main__":
    main()
