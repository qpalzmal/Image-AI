from imageai.Detection import ObjectDetection
import os

# execution_path = os.getcwd()

detector = ObjectDetection()
detector.setModelTypeAsRetinaNet()
detector.setModelPath("resnet50_coco_best_v2.0.1.h5")
detector.loadModel()
detections = detector.detectObjectsFromImage("image.jpg", "newimage.jpg")

for object in detections:
    # print(object)
    print(object["name"], ":", object["percentage_probability"], ":", object["box_points"])
    print("___________________________________________")
