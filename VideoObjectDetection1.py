from imageai.Detection import VideoObjectDetection
import cv2

camera = cv2.VideoCapture(0)
camera.

detector = VideoObjectDetection()
detector.setModelTypeAsTinyYOLOv3()
detector.setModelPath("yolo-tiny.h5")
detector.loadModel(detection_speed="flash")
detections = detector.detectObjectsFromVideo(input_file_path="Road traffic video for object recognition.mp4",
                                             output_file_path="REEEEEE.mp4",  # new video that has the boxes for objects
                                             # camera_input=camera,
                                             frames_per_second=60,
                                             minimum_percentage_probability=5)

print("REEEEEEEEEEEEEEEEEEEEE")
