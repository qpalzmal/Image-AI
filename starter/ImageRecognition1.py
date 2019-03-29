from imageai.Prediction.Custom import CustomImagePrediction
from imageai.Detection import ObjectDetection
# import os
import pprint

# execution_path = os.getcwd()  # gets the path of where the python file and model file are at


# DETECTION TO OUTPUT THE PREDICTION IN CONSOLE
prediction = CustomImagePrediction()

prediction.setModelTypeAsResNet()  # sets the model type of prediction as ResNet - one we used
prediction.setModelPath("idenprof_061-0.7933.h5")  # sets model path of prediction to the ai model file
prediction.setJsonPath("idenprof_model_class.json")  # sets the path of json file
prediction.loadModel(num_objects=10)

# DETECTION TO CREATE NEW IMAGES ON FOUND ITEMS
detector = ObjectDetection()
detector.setModelTypeAsRetinaNet()
detector.setModelPath("resnet50_coco_best_v2.0.1.h5")
detector.loadModel()
detections, path = detector.detectObjectsFromImage(input_image="image.jpg",  # takes in the input image
                                                   output_image_path="newimage.jpg",  # creates a new image
                                                   # creates new images from the each object
                                                   extract_detected_objects=True)


# DETECTION TO DRAW BOXES AROUND IN A NEW IMAGE
lidl_detector = ObjectDetection()
lidl_detector.setModelTypeAsRetinaNet()
lidl_detector.setModelPath("resnet50_coco_best_v2.0.1.h5")
lidl_detector.loadModel()
lidl_detections = lidl_detector.detectObjectsFromImage(input_image="image.jpg",  # takes in the input image
                                                       output_image_path="LIDLnewimage.jpg")  # creates a new image

# DETECTION TO OUTPUT THE PREDICTION IN CONSOLE
predictions, probabilities = prediction.predictImage(image_input="image.jpg", result_count=3)

for prediction, probability in zip(predictions, probabilities):
    print(prediction, ":", probability)

# DETECTION TO CREATE NEW IMAGES ON FOUND ITEMS
for eaobject, eapath in zip(detections, path):
    print("DECTECTION: ", eaobject, "PATH :", eapath)
    print("________________________________________")


# DETECTION TO DRAW BOXES AROUND IN A NEW IMAGE
for object in lidl_detections:
    #     pprint.pprint(object)
    #     # print("REE")
    print(object["name"], ":", object["percentage_probability"])
    print("___________________________________________________")

print(detections)


