from imageai.Prediction.Custom import CustomImagePrediction
from imageai.Detection import ObjectDetection
# import os
import pprint

# execution_path = os.getcwd()  # gets the path of where the python file and model file are at

prediction = CustomImagePrediction()

prediction.setModelTypeAsResNet()  # sets the model type of prediction as ResNet - one we used
prediction.setModelPath("idenprof_061-0.7933.h5")  # sets model path of prediction to the ai model file
prediction.setJsonPath("idenprof_model_class.json")  # sets the path of json file
prediction.loadModel(num_objects=10)

# print("AAAAAAAAA")

detector = ObjectDetection()
detector.setModelTypeAsRetinaNet()
detector.setModelPath("resnet50_coco_best_v2.0.1.h5")
detector.loadModel()
detections, path = detector.detectObjectsFromImage("image.jpg",  # takes in the input image
                                                   output_image_path="newimage.jpg",  # creates a new image
                                                   minimum_percentage_probability=25,
                                                   # minimum percentage needed to show
                                                   extract_detected_objects=True)  # creates new images from the each object

lidl_detector = ObjectDetection()
lidl_detector.setModelTypeAsRetinaNet()
lidl_detector.setModelPath("resnet50_coco_best_v2.0.1.h5")
lidl_detector.loadModel()
lidl_detections = lidl_detector.detectObjectsFromImage("image.jpg",  # takes in the input image
                                                       output_image_path="LIDLnewimage.jpg")  # creates a new image

# print("BBBBBBBBB")

predictions, probabilities = prediction.predictImage("image.jpg", result_count=3)

for prediction, probability in zip(predictions, probabilities):
    print(prediction, ":", probability)

for object in lidl_detections:
    #     pprint.pprint(object)
    #     # print("REE")
    print(object["name"], ":", object["percentage_probability"])
    print("___________________________________________________")

for eaobject, eapath in zip(detections, path):
    print("DECTECTION: ", eaobject, "PATH :", eapath)
    print("________________________________________")
