from imageai.Detection import VideoObjectDetection
# import cv2
from OpenCVCamera import *


# def EveryFrame(frame_number, output_array, output_count):
#     print("FOR FRAME: ", frame_number)
#     print(output_array)
#     print(output_count)
#     print("END OF FRAME: ", frame_number)


# camera = cv2.VideoCapture(0)

detector = VideoObjectDetection()
detector.setModelTypeAsRetinaNet()
detector.setModelPath("resnet50_coco_best_v2.0.1.h5")
# detector.loadModel(detection_speed="flash")
detector.loadModel()

# print("BEFORE CAMERA RELEASE")
# camera.release()
# print("AFTER CAMERA RELEASE")


show_webcam()

detections = detector.detectObjectsFromVideo(
                                             input_file_path="Sounds of New York City.mp4",
                                             output_file_path="MODIFIED VIDEO",
                                             frames_per_second=10,
                                             minimum_percentage_probability=50,
                                             log_progress=True,
                                             # camera_input=camera
                                             # return_detected_frame=True,
                                             # per_frame_function=EveryFrame
                                             )

# for object in detections:
#     print(object["name"], ":", object["percentage_probability"])

# camera.release()
print("REEEEEEEEEEEEEEEEEEEEE")
