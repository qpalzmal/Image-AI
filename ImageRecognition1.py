from imageai.Prediction.Custom import CustomImagePrediction
import os

execution_path = os.getcwd()  # gets the path of where the python file and model file are at

prediction = CustomImagePrediction()
prediction.setModelTypeAsResNet()  # sets the model type of prediction as ResNet - one we used
prediction.setModelPath("idenprof_061-0.7933.h5")  # sets model path of prediction to the ai model file
prediction.setJsonPath("idenprof_model_class.json")  # sets the path of json file
prediction.loadModel(num_objects=10)

predictions, probabilities = prediction.predictImage("image.jpg", result_count=3)

for eachPrediction, eachProbability in zip(predictions, probabilities):
    print(eachPrediction, ":", eachProbability)
