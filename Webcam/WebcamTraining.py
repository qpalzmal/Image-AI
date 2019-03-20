from imageai.Prediction.Custom import ModelTraining

model_trainer = ModelTraining()

'''
Use SqueezeNet as it has the fastest prediction so it works well with webcam to simulate realtime
sets model type to "SqueezeNet", other options are "ResNet", "InceptionV3", DenseNet"
SqueezeNet = fastest prediction - mid accuracy
ResNet = fast prediction - high accuracy
InceptionV3 = slow prediction - higher accuracy
DenseNet = slowest prediction - highest accuracy
'''
model_trainer.setModelTypeAsSqueezeNet()

# sets data directory where the dataset is stored
model_trainer.setDataDirectory("Webcam")

model_trainer.trainModel(num_objects=8,  # the number of different type of classes in the dataset
                         num_experiments=200,  # number of times model trainer studies the images
                         enhance_data=True,  # creates modified copies of images to improve accuracy-works best <1k imgs
                         batch_size=32,  # number of images model will study at once
                         show_network_summary=True)  # shows the structure of model type used
