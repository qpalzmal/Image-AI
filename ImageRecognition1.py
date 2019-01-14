from imageai.Prediction.Custom import CustomImagePrediction
from imageai.Detection import ObjectDetection
# import os

# execution_path = os.getcwd()  # gets the path of where the python file and model file are at

prediction = CustomImagePrediction()

prediction.setModelTypeAsResNet()  # sets the model type of prediction as ResNet - one we used
prediction.setModelPath("idenprof_061-0.7933.h5")  # sets model path of prediction to the ai model file
prediction.setJsonPath("idenprof_model_class.json")  # sets the path of json file
prediction.loadModel(num_objects=10)

detector = ObjectDetection()
detector.setModelTypeAsRetinaNet()
detector.setModelPath("resnet50_coco_best_v2.0.1.h5")
detector.loadModel()
detections = detector.detectObjectsFromImage("image.jpg", "newimage.jpg")

predictions, probabilities = prediction.predictImage("image.jpg", result_count=3)

for prediction, probability in zip(predictions, probabilities):
    print(prediction, ":", probability)
